from transformers import pipeline, Conversation

class ChatbotService:
    def __init__(self, poll_service):
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
        self.poll_service = poll_service
        self.historial = {}  # Opcional: historial por username

    def responder(self, username, mensaje):
        # Opcional: mantener historial por usuario
        if username not in self.historial:
            self.historial[username] = []

        # Verificar palabras clave relacionadas con encuestas
        if "ganando" in mensaje or "resultados" in mensaje:
            # Llamar a PollService para obtener resultados parciales
            encuestas = self.poll_service.encuesta_repo.cargar_todas_encuestas()
            activas = [e for e in encuestas if e.estado == "activa"]
            if not activas:
                return "No hay encuestas activas en este momento."
            resultados = self.poll_service.get_partial_results(activas[0].id)
            respuesta = "Resultados parciales:\n"
            for opcion, datos in resultados.items():
                respuesta += f"{opcion}: {datos['conteo']} votos ({datos['porcentaje']:.2f}%)\n"
            return respuesta

        if "falta" in mensaje or "tiempo" in mensaje:
            # Llamar a PollService para calcular tiempo restante
            encuestas = self.poll_service.encuesta_repo.cargar_todas_encuestas()
            activas = [e for e in encuestas if e.estado == "activa"]
            if not activas:
                return "No hay encuestas activas en este momento."
            tiempo_restante = activas[0].duracion - (datetime.now() - activas[0].creada_en).seconds
            return f"Faltan {tiempo_restante} segundos para que termine la encuesta."

        # Enviar mensaje al pipeline de IA para otros casos
        self.historial[username].append({"usuario": mensaje})
        conversation = Conversation(mensaje)  # Create a Conversation object
        respuesta = self.chatbot(conversation).generated_responses[-1]  # Get the latest response
        self.historial[username].append({"bot": respuesta})
        return respuesta
