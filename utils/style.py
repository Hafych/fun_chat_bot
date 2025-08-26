# utils/style.py
from colorama import Fore, Style
from termcolor import colored
from fabulous import text, image

def gradient_text(msg):
    return text.Text(msg)

def print_gradient(msg):
    print(gradient_text(msg))

def colored_print(msg, color="white", effect=None):
    print(colored(msg, color, attrs=effect if effect else []))

def emoji_wrap(text, emote):
    import emoji
    return f"{emoji.emojize(emote)} {text} {emoji.emojize(emote)}"