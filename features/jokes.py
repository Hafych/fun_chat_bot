from pyjokes import get_joke
from utils.style import colored_print


def tell_joke():
    try:
        joke = get_joke(language='en', category='neutral')
        colored_print(f"😂 {joke}", "yellow")
    except:
        colored_print("Не удалось получить анекдот :(", "red")