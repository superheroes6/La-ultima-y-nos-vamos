import gradio as gr
from src.services.chatbot_service import ChatbotService
from src.services.poll_service import PollService
from src.repositories.encuesta_repo import EncuestaRepository
from src.controllers.ui_controller import UIController

encuesta_repo = EncuestaRepository("encuestas.json")
poll_service = PollService(encuesta_repo, None, None, None)
chatbot_service = ChatbotService(poll_service)
nft_service = None

ui_controller = UIController(poll_service, nft_service, chatbot_service)

def chatbot_response(username, mensaje):
    return chatbot_service.responder(username, mensaje)

with gr.Blocks() as gradio_app:
    gr.Markdown("# Chatbot IA - Encuestas Interactivas")
    username = gr.Textbox(label="Nombre de usuario", placeholder="Introduce tu nombre de usuario", value="usuario123")
    chat = gr.ChatInterface(fn=lambda mensaje: chatbot_service.responder(username.value, mensaje))
    
    with gr.Tab("Encuestas"):
        encuesta_list = gr.Dataframe(headers=["ID", "Pregunta", "Estado"], interactive=False)
        listar_encuestas_button = gr.Button("Listar Encuestas")
        listar_encuestas_button.click(
            fn=lambda: ui_controller.listar_encuestas(),
            inputs=[],
            outputs=encuesta_list
        )
        poll_id = gr.Textbox(label="ID de Encuesta")
        opcion = gr.Textbox(label="Opción")
        votar_result = gr.Textbox(label="Resultado de Votación", interactive=False)
        votar_button = gr.Button("Votar")
        votar_button.click(
            fn=lambda poll_id, opcion: ui_controller.votar(poll_id, username.value, opcion),
            inputs=[poll_id, opcion],
            outputs=votar_result
        )
    
    with gr.Tab("Galería de Tokens"):
        token_gallery = gr.Dataframe(headers=["Token ID", "Encuesta", "Opción", "Emitido"], interactive=False)
        listar_tokens_button = gr.Button("Listar Tokens")
        listar_tokens_button.click(
            fn=lambda: ui_controller.listar_tokens(username.value),
            inputs=[],
            outputs=token_gallery
        )

if __name__ == "__main__": 
    gradio_app.launch()
