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

def listar_tokens(username):
    tokens = chatbot_service.poll_service.nft_service.nft_repo.cargar_tokens()
    tokens_usuario = [token for token in tokens if token.owner == username]
    return [{"Token ID": token.token_id, "Encuesta": token.poll_id, "Opción": token.option, "Emitido": token.issued_at} for token in tokens_usuario]

# Interfaz de chat
with gr.Blocks() as gradio_app:
    gr.Markdown("# Chatbot IA - Encuestas Interactivas")
    username = gr.Textbox(label="Nombre de usuario", placeholder="Ingresa tu nombre de usuario")
    chat = gr.ChatInterface(fn=lambda mensaje: chatbot_response(username.value, mensaje))
    with gr.Tab("Galería de Tokens"):
        username = gr.Textbox(label="Nombre de usuario", placeholder="Ingresa tu nombre de usuario")
        token_gallery = gr.Dataframe(headers=["Token ID", "Encuesta", "Opción", "Emitido"], interactive=False)
        listar_button = gr.Button("Listar Tokens")
        listar_button.click(fn=lambda username: listar_tokens(username), inputs=username, outputs=token_gallery)

# Lanzar la aplicación
if __name__ == "__main__":
    gradio_app.launch()
