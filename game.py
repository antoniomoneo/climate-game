def welcome_player(language='es'):
    """Show a welcome message in the selected language."""
    messages = {
        'es': '¡Hola! Bienvenido/a al juego Tangible Climate',
        'en': 'Hello! Welcome to Tangible Climate'
    }
    print(messages.get(language, messages['es']))


def main():
    welcome_player()
    input('Introduce una palabra: ')

if __name__ == '__main__':
    main()
