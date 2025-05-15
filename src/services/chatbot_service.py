from transformers import pipeline
import time

class ChatbotService:
    def __init__(self, poll_service):
        # Cambiar el pipeline a text2text-generation para mayor compatibilidad
        self.chatbot = pipeline("text2text-generation", model="t5-small")
        self.poll_service = poll_service
        self.historial = {}  # Opcional: historial por username

    def responder(self, username, mensaje):
        # Verificar palabras clave relacionadas con encuestas
        if "ganando" in mensaje or "resultados" in mensaje:
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
            tiempo_actual = time.time()
            tiempo_restante = activas[0].duracion - (tiempo_actual - activas[0].creada_en.timestamp())
            return f"Faltan {int(tiempo_restante)} segundos para que termine la encuesta."

        # Enviar mensaje al pipeline de IA para otros casos
        self.historial[username].append({"usuario": mensaje})
        respuesta = self.chatbot(mensaje, max_length=50)[0]["generated_text"]  # Use text-generation
        self.historial[username].append({"bot": respuesta})
        return respuesta
