import os

def clear_console(os_name):
    """ Función que limpia la consola de comandos de acuerdo al
        sistema operativo en el que se ejecuta:
        'cls' para 'windows'
        'clear' para otros OS
    """
    if os_name == "windows":
        os.system("cls")
    else:
        os.system("clear")
