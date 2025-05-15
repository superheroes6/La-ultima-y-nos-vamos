# La última y nos vamos

## Introducción y contexto
En el entorno actual del entretenimiento digital, el streaming ha evolucionado más allá de la simple difusión de partidas de videojuegos o eventos en vivo: los creadores de contenido buscan constantemente nuevas formas de involucrar a su audiencia, ofrecer experiencias interactivas y premiar la fidelidad de sus seguidores. 

Al mismo tiempo, avances en inteligencia artificial conversacional y la emergente cultura de tokens no fungibles (NFTs) abren la puerta a construir plataformas que combinen votaciones en tiempo real, chatbots capaces de conversar de manera natural y economía digital simulada mediante coleccionables.

Con este escenario como telón de fondo, se plantea el desarrollo de una aplicación de votaciones interactivas para streamers —tanto mediante línea de comandos (CLI) para la administración del canal como con una interfaz web ligera (usando Gradio) para la audiencia— que incorpore tres módulos principales:

1. **Sistema de encuestas en vivo**: crea, administra y cierra encuestas con tiempo limitado, permitiendo a los espectadores votar en tiempo real.
2. **Chatbot IA**: integra un modelo preentrenado de Hugging Face Transformers para responder preguntas de los espectadores sobre las encuestas, el stream y cualquier tema relevante.
3. **Tokens NFT simulados**: cada voto emitido genera un “token coleccionable” único, que los usuarios podrán ver en una galería y transferir entre sí.

El objetivo de este ejercicio es que el alumno ponga en práctica conceptos avanzados de Programación Orientada a Objetos (POO), patrones de diseño (Observer, Factory, Strategy, etc.), arquitectura modular y buenas prácticas de ingeniería de software (persistencia desacoplada, pruebas unitarias, documentación), al tiempo que construye una plataforma atractiva y moderna.

## Instrucciones de instalación
Ejecuta el siguiente comando para instalar las dependencias:
```
pip install -r requirements.txt
```

## Cómo ejecutar en modo CLI
Ejecuta el siguiente comando:
```
python src/app.py
```

## Cómo lanzar la UI
Ejecuta el siguiente comando:
```
python src/app.py --ui
```

## Descripción de patrones y módulos
Este proyecto utiliza patrones de diseño como Observer, Factory y Strategy. Los módulos están organizados en carpetas para facilitar la escalabilidad y el mantenimiento.
