class UIController:
    def __init__(self, poll_service, nft_service, chatbot_service):
        self.poll_service = poll_service
        self.nft_service = nft_service
        self.chatbot_service = chatbot_service

    def listar_encuestas(self):
        encuestas = self.poll_service.encuesta_repo.cargar_todas_encuestas()
        return [{"ID": e.id, "Pregunta": e.pregunta, "Estado": e.estado} for e in encuestas]

    def votar(self, poll_id, username, opcion):
        try:
            self.poll_service.votar(poll_id, username, opcion)
            return "Voto registrado correctamente."
        except ValueError as e:
            return f"Error: {e}"

    def listar_tokens(self, username):
        tokens = self.nft_service.nft_repo.cargar_tokens()
        tokens_usuario = [token for token in tokens if token.owner == username]
        return [{"Token ID": token.token_id, "Encuesta": token.poll_id, "Opción": token.option, "Emitido": token.issued_at} for token in tokens_usuario]
