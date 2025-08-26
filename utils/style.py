# utils/style.py
from colorama import init, Fore, Style
from termcolor import colored
import emoji
init(autoreset=True)

def print_gradient(msg):
    """Простая альтернатива: цветной текст"""
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ""
    for i, char in enumerate(msg):
        color = colors[i % len(colors)]
        colored_text += colored(char, color)
    print(colored_text)

# Остальные функции остаются
def colored_print(msg, color="white", attrs=None):
    print(colored(msg, color, attrs=attrs if attrs else []))

def emoji_wrap(text, emote):
    return f"{emoji.emojize(emote)} {text} {emoji.emojize(emote)}"