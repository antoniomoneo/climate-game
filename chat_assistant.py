import json
import os
import openai


def load_game_data(json_path: str, txt_path: str):
    """Load game skeleton data and developer instructions."""
    with open(json_path, "r", encoding="utf-8") as f:
        game_data = json.load(f)
    with open(txt_path, "r", encoding="utf-8") as f:
        instructions = f.read()
    return game_data, instructions


def build_system_prompt(game_data: dict, instructions: str, language: str = "es") -> str:
    """Combine the text and JSON content into a single system prompt."""
    intro = game_data.get("introduccion", "")
    characters = "\n".join(
        f"- {c['nombre']}: {c['descripcion']}" for c in game_data.get("personajes", [])
    )
    return (
        f"{instructions}\n\n"
        f"{intro}\n\n"
        f"Personajes:\n{characters}\n\n"
        f"Responde en {language}. Inicia el juego actuando como la IA Científica, "
        "guiando al Jugador."
    )


def chat_with_assistant(system_prompt: str, model: str = "gpt-3.5-turbo") -> None:
    """Launch an interactive chat session using OpenAI API."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key

    messages = [{"role": "system", "content": system_prompt}]
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print()
            break
        if user_input.lower() in {"salir", "exit", "quit"}:
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model=model, messages=messages)
        reply = response.choices[0].message.content
        print(f"Assistant: {reply}")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    data, notes = load_game_data("esqueleto_cambio_climatico.json", "instrucciones_esqueleto.txt")
    prompt = build_system_prompt(data, notes, language="es")
    chat_with_assistant(prompt)
