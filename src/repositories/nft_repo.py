import json

class NFTRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_token(self, token):
        with open(self.file_path, 'w') as file:
            json.dump(token.__dict__, file)

    def cargar_tokens(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data
