import gradio as gr
from src.services.chatbot_service import ChatbotService
from src.services.poll_service import PollService
from src.repositories.encuesta_repo import EncuestaRepository

# Configurar servicios
encuesta_repo = EncuestaRepository("encuestas.json")
poll_service = PollService(encuesta_repo, None, None, None)  # Ajustar según implementación
chatbot_service = ChatbotService(poll_service)

# Función de respuesta para Gradio
def chatbot_response(username, mensaje):
    return chatbot_service.responder(username, mensaje)

# Interfaz de chat
with gr.Blocks() as gradio_app:
    gr.Markdown("# Chatbot IA - Encuestas Interactivas")
    username = gr.Textbox(label="Nombre de usuario", placeholder="Ingresa tu nombre de usuario")
    chat = gr.ChatInterface(fn=lambda mensaje: chatbot_response(username.value, mensaje))

# Lanzar la aplicación
if __name__ == "__main__":
    gradio_app.launch()
