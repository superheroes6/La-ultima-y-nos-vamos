from src.ui.gradio_app import gradio_app

def main():
    print("Iniciando la interfaz gráfica...")
    try:
        gradio_app.launch(share=True)
    except Exception as e:
        print(f"Error al iniciar la interfaz gráfica: {e}")

if __name__ == "__main__":
    main()
