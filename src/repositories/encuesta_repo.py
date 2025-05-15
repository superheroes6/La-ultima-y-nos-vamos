import json

class EncuestaRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_encuesta(self, encuesta):
        with open(self.file_path, 'w') as file:
            json.dump(encuesta.__dict__, file)

    def cargar_encuesta(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data
