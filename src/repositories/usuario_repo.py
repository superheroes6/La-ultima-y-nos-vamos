import json

class UsuarioRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_usuario(self, usuario):
        with open(self.file_path, 'w') as file:
            json.dump(usuario.__dict__, file)

    def cargar_usuario(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data
