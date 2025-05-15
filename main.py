import argparse
from src.controllers.cli_controller import CLIController
from src.ui.gradio_app import gradio_app
from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.nft_repo import NFTRepository
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="La última y nos vamos - Plataforma de votaciones interactivas")
    parser.add_argument("--ui", action="store_true", help="Lanzar la interfaz gráfica (Gradio)")
    args = parser.parse_args()

    # Initialize repositories
    encuesta_repo = EncuestaRepository("data/encuestas.json")
    usuario_repo = UsuarioRepository("data/usuarios.json")
    nft_repo = NFTRepository("data/nfts.json")

    # Initialize services
    nft_service = NFTService(nft_repo)
    poll_service = PollService(encuesta_repo, None, nft_service, None)
    user_service = UserService(usuario_repo)
    chatbot_service = ChatbotService(poll_service)

    # CLI or UI mode
    if args.ui:
        print("Iniciando la interfaz gráfica...")
        gradio_app.launch()
    else:
        print("Iniciando la interfaz de línea de comandos...")
        usuario_actual = input("Ingresa tu nombre de usuario: ")
        cli_controller = CLIController(nft_service, usuario_actual)
        while True:
            print("\nComandos disponibles:")
            print("1. Ver mis tokens")
            print("2. Transferir token")
            print("3. Salir")
            comando = input("Selecciona una opción: ")
            if comando == "1":
                cli_controller.mis_tokens()
            elif comando == "2":
                token_id = input("Ingresa el ID del token: ")
                nuevo_owner = input("Ingresa el nuevo propietario: ")
                cli_controller.transferir_token(token_id, nuevo_owner)
            elif comando == "3":
                print("Saliendo...")
                break
            else:
                print("Comando no reconocido. Intenta de nuevo.")

if __name__ == "__main__":
    main()
