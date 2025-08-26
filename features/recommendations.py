# features/recommendations.py
from prettytable import PrettyTable
from utils.style import colored_print, emoji_wrap
import random

MOVIES = {
    'action': ['Mad Max', 'John Wick', 'Die Hard'],
    'comedy': ['Superbad', 'Anchorman', 'The Hangover'],
    'horror': ['The Conjuring', 'Hereditary', 'Get Out']
}

MUSIC = {
    'rock': ['Bohemian Rhapsody', 'Stairway to Heaven'],
    'pop': ['Blinding Lights', 'Levitating'],
    'jazz': ['Take Five', 'So What']
}

GAMES = {
    'action': ['Call of Duty', 'Assassin’s Creed'],
    'rpg': ['The Witcher 3', 'Skyrim'],
    'strategy': ['Civilization VI', 'XCOM 2']
}

def show_table(data, title):
    table = PrettyTable()
    table.field_names = ["Жанр", "Примеры"]
    for genre, items in data.items():
        table.add_row([genre.capitalize(), ", ".join(items[:2]) + "..."])
    table.align = "l"
    colored_print(f"\n{emoji_wrap(title, ':sparkles:')}", "magenta")
    print(table)

def get_choice(data, prompt):
    show_table(data, prompt)
    while True:
        choice = input(f"Выберите жанр: ").lower()
        if choice in data:
            return data[choice]
        colored_print("❌ Нет такого жанра!", "red")

def recommend_movie():
    result = random.choice(get_choice(MOVIES, "Фильмы"))
    colored_print(f"🎬 Рекомендую: {result}", "green")

def recommend_music():
    result = random.choice(get_choice(MUSIC, "Музыка"))
    colored_print(f"🎵 Попробуйте: {result}", "cyan")

def recommend_game():
    result = random.choice(get_choice(GAMES, "Игры"))
    colored_print(f"🎮 Поиграйте в: {result}", "blue")