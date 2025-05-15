from src.models.token_nft import TokenNFT

class NFTService:
    def __init__(self, nft_repo):
        self.nft_repo = nft_repo

    def mint_token(self, owner, poll_id, option):
        token = TokenNFT(None, owner, poll_id, option)
        self.nft_repo.guardar_token(token)

    def transfer_token(self, token_id, nuevo_owner, usuario_actual):
        tokens = self.nft_repo.cargar_tokens()
        for token in tokens:
            if token.token_id == token_id:
                if token.owner != usuario_actual:
                    raise ValueError("No tienes permiso para transferir este token.")
                token.owner = nuevo_owner
                self.nft_repo.actualizar_token(token_id, nuevo_owner)
                return
        raise ValueError("Token no encontrado.")
