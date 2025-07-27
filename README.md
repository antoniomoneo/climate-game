# climate-game

Este proyecto contiene un juego de ejemplo llamado **Tangible Climate**.

## Uso local

Para probar la versión local simple ejecuta:

```bash
python game.py
```

Esto mostrará un breve mensaje de bienvenida.

## Integración con ChatGPT

El archivo `chat_assistant.py` permite jugar utilizando la API de OpenAI para generar las respuestas de la IA Científica. Para utilizarlo es necesario definir la variable de entorno `OPENAI_API_KEY` con una clave válida.

```bash
export OPENAI_API_KEY=tu_clave
python chat_assistant.py
```

El script cargará la configuración desde `esqueleto_cambio_climatico.json` y las instrucciones de `instrucciones_esqueleto.txt` para iniciar la conversación.
