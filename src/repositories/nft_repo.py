import csv
from src.models.token_nft import TokenNFT

class NFTRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def guardar_token(self, token):
        # Append a new token to the CSV file
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([token.token_id, token.owner, token.poll_id, token.option, token.issued_at])

    def cargar_tokens(self):
        # Load all tokens from the CSV file
        tokens = []
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    tokens.append(TokenNFT(token_id=row[0], owner=row[1], poll_id=row[2], option=row[3], issued_at=row[4]))
        except FileNotFoundError:
            pass  # Return an empty list if the file does not exist
        return tokens

    def actualizar_token(self, token_id, nuevo_owner):
        # Update the owner of a token in the CSV file
        tokens = self.cargar_tokens()
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for token in tokens:
                if token.token_id == token_id:
                    token.owner = nuevo_owner
                writer.writerow([token.token_id, token.owner, token.poll_id, token.option, token.issued_at])
