from datetime import datetime
from src.models.encuesta import Encuesta  # Import the Encuesta class

class PollService:
    def __init__(self, encuesta_repo):
        self.encuesta_repo = encuesta_repo

    def crear_encuesta(self, id, pregunta, opciones, duracion):
        encuesta = Encuesta(id, pregunta, opciones, duracion)
        self.encuesta_repo.guardar_encuesta(encuesta)

    def registrar_voto(self, encuesta_id, opcion):
        encuesta = self.encuesta_repo.cargar_encuesta()
        encuesta.registrar_voto(opcion)
        self.encuesta_repo.guardar_encuesta(encuesta)

    def cerrar_encuesta(self, encuesta_id):
        encuesta = self.encuesta_repo.cargar_encuesta()
        encuesta.cerrar()
        self.encuesta_repo.guardar_encuesta(encuesta)
