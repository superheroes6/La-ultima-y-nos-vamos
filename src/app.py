import argparse
from src.ui.gradio_app import gradio_app
from src.controllers.cli_controller import CLIController
from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.nft_repo import NFTRepository
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.patterns.observer import Observer

def main():
    parser = argparse.ArgumentParser(description="Aplicación de Encuestas Interactivas")
    parser.add_argument("--ui", action="store_true", help="Iniciar la interfaz gráfica (Gradio)")
    args = parser.parse_args()

    encuesta_repo = EncuestaRepository("data/encuestas.json")
    usuario_repo = UsuarioRepository("data/usuarios.json")
    nft_repo = NFTRepository("data/nfts.csv")

    observer = Observer()
    nft_service = NFTService(nft_repo)
    poll_service = PollService(encuesta_repo, None, nft_service, observer)
    user_service = UserService(usuario_repo)
    chatbot_service = ChatbotService(poll_service)

    observer.registrar(nft_service)

    if args.ui:
        gradio_app.launch(share=True)
    else:
        cli_controller = CLIController(nft_service, "admin")
        cli_controller.run()

if __name__ == "__main__":
    main()
