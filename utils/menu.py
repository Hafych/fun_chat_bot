# utils/menu.py
from art import text2art
from tqdm import tqdm
from time import sleep
from utils.style import print_gradient, colored_print, emoji_wrap

def loading_screen():
    print_gradient("FunChatBot")
    for _ in tqdm(range(100), desc="Загрузка бота", ncols=100, bar_format="{l_bar}{bar}|"):
        sleep(0.02)
    print()

def show_main_menu():
    colored_print("\n" + "="*60, "blue")
    print(text2art("FunBot", font="small"))
    colored_print(emoji_wrap("🌟 Главное меню", ":star:"), "cyan", ["bold"])
    colored_print("="*60, "blue")

    print(emoji_wrap("1. 🎬 Фильмы", ":clapper_board:"))
    print(emoji_wrap("2. 🎵 Музыка", ":musical_note:"))
    print(emoji_wrap("3. 🎮 Игры", ":video_game:"))
    print(emoji_wrap("4. 😂 Анекдот", ":face_with_tears_of_joy:"))
    print(emoji_wrap("5. 📖 Факт", ":books:"))
    print(emoji_wrap("6. 🎲 Камень-Ножницы-Бумага", ":rock:"))
    print(emoji_wrap("7. 🔢 Угадай число", ":1234:"))
    print(emoji_wrap("8. 🎰 Поле чудес", ":ferris_wheel:"))
    colored_print(emoji_wrap("exit — выход", ":door:"), "yellow")

    return input(Fore.GREEN + "Выберите пункт: " + Style.RESET_ALL)