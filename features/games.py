from utils.style import colored_print, emoji_wrap
import random


def play_rps():
    choices = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    colored_print("\n" + emoji_wrap("Камень-Ножницы-Бумага", ":game_die:"), "cyan")
    user = input("Выберите (rock/paper/scissors): ").lower()
    if user not in choices:
        colored_print("❌ Неверный выбор!", "red")
        return
    bot = random.choice(list(choices.keys()))
    print(f"Вы: {choices[user]} vs Бот: {choices[bot]}")
    result = check_rps(user, bot)
    colored_print(result, "magenta")


def check_rps(user, bot):
    win = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper')
    }
    if user == bot:
        return "🤝 Ничья!"
    elif (user, bot) in win:
        return "🎉 Вы выиграли!"
    else:
        return "💀 Вы проиграли!"


def play_guess_number():
    colored_print("\n" + emoji_wrap("Угадай число (1-10)", ":1234:"), "green")
    number = random.randint(1, 10)
    try:
        guess = int(input("Ваш вариант: "))
        if guess == number:
            colored_print("🎉 Угадали! 🎉", "yellow", ["bold"])
        else:
            colored_print(f"❌ Не угадали. Было: {number}", "red")
    except ValueError:
        colored_print("❗ Это не число!", "red")


def play_wheel_of_fortune():
    words = ["python", "fun", "code", "music", "game", "variable", "function", "class", "object", "method", 
             "attribute", "parameter", "argument", "return", "value", "integer", "float", "string", "boolean", 
             "list", "tuple", "dictionary", "set", "index", "slice", "loop", "for", "while", "if", "elif", "else", 
             "break", "continue", "pass", "None", "True", "False", "import", "module", "package", "library", "print", 
             "input", "type", "isinstance", "len", "range", "enumerate", "zip", "map", "filter", "lambda", 
             "comprehension", "generator", "iterator", "yield", "next", 
             "iterable", "mutable", "immutable", "hashable", "key", "value", "item", "syntax", "indentation", 
             "block", "scope", "global", "local", "closure", "nested", "recursion", "base case", "stack", "overflow", "error", 
             "exception", "try", "except", "finally", "raise", "assert", "debug", "traceback", "name", "namespace", "global", 
             "enclosing", "local", "PEP", "style", "comment", "docstring", "annotation", "def", "return", "class", 
             "self", "cls", "super", "inheritance", "polymorphism", "encapsulation", "abstraction", "override", "overload", 
             "dunder", "property", "getter", "setter", "decorator",
             "with", "open", "file", "read", "write", "close", "encoding", "newline", "buffer", "mode", "JSON", "parse", 
             "dump", "load", "encode", "decode", "API", "request", "response", "HTTP", "GET", "POST", "pip", "install", 
             "venv", "activate", "git", "commit", "push", "pull", "clone", "repository", "async", "await", "thread", 
             "multiprocessing", "concurrency", "parallelism", "callback"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    colored_print(f"\n{emoji_wrap('Поле чудес!', ':ferris_wheel:')} Угадайте слово: {' '.join(guessed)}", "blue")
    while attempts > 0 and "_" in guessed:
        letter = input(f"Буква (осталось {attempts}): ").lower()
        if len(letter) != 1 or not letter.isalpha():
            colored_print("❗ Одна буква!", "yellow")
            continue
        if letter in word:
            for i, c in enumerate(word):
                if c == letter:
                    guessed[i] = letter
            colored_print(f"✅ {letter} есть! {''.join(guessed)}", "green")
        else:
            attempts -= 1
            colored_print("❌ Нет такой буквы.", "red")
    if "_" not in guessed:
        colored_print(f"🎉 Вы угадали: {word}!", "magenta", ["bold"])
    else:
        colored_print(f"💀 Было: {word}", "red")