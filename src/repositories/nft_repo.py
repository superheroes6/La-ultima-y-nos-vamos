import json
from src.models.token_nft import TokenNFT

class NFTRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_token(self, token):
        tokens = self.cargar_tokens()
        tokens.append(token.__dict__)
        with open(self.file_path, 'w') as file:
            json.dump(tokens, file)

    def cargar_tokens(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [TokenNFT(**token) for token in data]
        except FileNotFoundError:
            return []

    def actualizar_token(self, token_id, nuevo_owner):
        tokens = self.cargar_tokens()
        for token in tokens:
            if token.token_id == token_id:
                token.owner = nuevo_owner
        with open(self.file_path, 'w') as file:
            json.dump([token.__dict__ for token in tokens], file)
