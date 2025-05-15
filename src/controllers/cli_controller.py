class CLIController:
    def __init__(self, nft_service, usuario_actual):
        self.nft_service = nft_service
        self.usuario_actual = usuario_actual

    def mis_tokens(self):
        tokens = self.nft_service.nft_repo.cargar_tokens()
        tokens_usuario = [token for token in tokens if token.owner == self.usuario_actual]
        for token in tokens_usuario:
            print(f"Token ID: {token.token_id}, Encuesta: {token.poll_id}, Opción: {token.option}, Emitido: {token.issued_at}")

    def transferir_token(self, token_id, nuevo_owner):
        try:
            self.nft_service.transfer_token(token_id, nuevo_owner, self.usuario_actual)
            print(f"Token {token_id} transferido a {nuevo_owner}.")
        except ValueError as e:
            print(f"Error: {e}")
