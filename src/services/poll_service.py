from datetime import datetime, timedelta
from src.models.encuesta import Encuesta
from src.models.voto import Voto
from src.models.token_nft import TokenNFT
import uuid

class PollService:
    def __init__(self, encuesta_repo, voto_repo, nft_service, observer):
        self.encuesta_repo = encuesta_repo
        self.voto_repo = voto_repo
        self.nft_service = nft_service
        self.observer = observer

    def crear_encuesta(self, pregunta, opciones, duracion_segundos, tipo="simple"):
        encuesta_id = str(uuid.uuid4())
        encuesta = Encuesta(encuesta_id, pregunta, opciones, duracion_segundos)
        encuesta.tipo = tipo
        self.encuesta_repo.guardar_encuesta(encuesta)

    def votar(self, poll_id, username, opcion):
        encuesta = self.encuesta_repo.cargar_encuesta()
        if encuesta.id != poll_id or encuesta.estado != "activa":
            raise ValueError("La encuesta no existe o no está activa.")
        if username in self.voto_repo.obtener_votantes(poll_id):
            raise ValueError("El usuario ya ha votado en esta encuesta.")
        if isinstance(opcion, list) and encuesta.tipo != "multiple":
            raise ValueError("Esta encuesta no permite múltiples opciones.")

        # Registrar voto
        voto = Voto(username, opcion)
        self.voto_repo.registrar_voto(poll_id, voto)
        encuesta.registrar_voto(opcion)
        self.encuesta_repo.guardar_encuesta(encuesta)

        # Generar token NFT
        timestamp = datetime.now()
        token_metadata = {
            "poll_id": poll_id,
            "opcion": opcion,
            "timestamp": timestamp.isoformat()
        }
        token = TokenNFT(str(uuid.uuid4()), token_metadata, username)
        self.nft_service.generar_token(token)
        self.nft_service.mint_token(username, poll_id, opcion)  # Mint token after voting

    def verificar_cierre_automatico(self):
        encuestas = self.encuesta_repo.cargar_todas_encuestas()
        for encuesta in encuestas:
            if encuesta.estado == "activa" and datetime.now() > encuesta.creada_en + timedelta(seconds=encuesta.duracion):
                self.cerrar_encuesta(encuesta.id)

    def cerrar_encuesta(self, poll_id):
        encuesta = self.encuesta_repo.cargar_encuesta()
        if encuesta.id != poll_id:
            raise ValueError("La encuesta no existe.")
        encuesta.cerrar()
        self.encuesta_repo.guardar_encuesta(encuesta)
        self.observer.notificar(encuesta)

    def get_partial_results(self, poll_id):
        encuesta = self.encuesta_repo.cargar_encuesta()
        if encuesta.id != poll_id:
            raise ValueError("La encuesta no existe.")
        total_votos = sum(encuesta.votos.values())
        return {
            opcion: {
                "conteo": conteo,
                "porcentaje": (conteo / total_votos * 100) if total_votos > 0 else 0
            }
            for opcion, conteo in encuesta.votos.items()
        }

    def get_final_results(self, poll_id):
        encuesta = self.encuesta_repo.cargar_encuesta()
        if encuesta.id != poll_id or encuesta.estado != "cerrada":
            raise ValueError("La encuesta no existe o no está cerrada.")
        return self.get_partial_results(poll_id)

    def resolver_desempate(self, encuesta, strategy):
        if encuesta.estado != "cerrada":
            raise ValueError("La encuesta debe estar cerrada para resolver desempates.")
        return strategy.resolve(encuesta)
