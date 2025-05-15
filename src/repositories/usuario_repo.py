import json

class UsuarioRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_usuario(self, usuarios):
        with open(self.file_path, 'w') as file:
            json.dump(usuarios, file)

    def cargar_usuario(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Retornar un diccionario vacío si el archivo no existe
