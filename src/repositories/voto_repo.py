import json

class VotoRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def registrar_voto(self, poll_id, voto):
        votos = self.cargar_votos()
        if poll_id not in votos:
            votos[poll_id] = []
        votos[poll_id].append(voto.__dict__)
        self.guardar_votos(votos)

    def obtener_votantes(self, poll_id):
        votos = self.cargar_votos()
        return [voto["usuario"] for voto in votos.get(poll_id, [])]

    def cargar_votos(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def guardar_votos(self, votos):
        with open(self.file_path, 'w') as file:
            json.dump(votos, file)
