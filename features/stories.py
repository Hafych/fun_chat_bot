# features/stories.py
from utils.style import colored_print, emoji_wrap
import random

FACTS = [
    "Медузы существуют дольше, чем динозавры.",
    "У осьминога три сердца.",
    "В космосе нельзя рыгать.",
    "Бананы — это ягоды, а клубника — нет."
]

def tell_fact():
    fact = random.choice(FACTS)
    colored_print(f"{emoji_wrap('📖 Интересный факт', ':open_book:')} {fact}", "blue")