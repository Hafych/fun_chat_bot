from colorama import init
from utils.menu import show_main_menu, loading_screen
from features import recommendations, jokes, stories, games, tictactoe

init(autoreset=True)


def navigate(choice):
    if choice == '1':
        recommendations.recommend_movie()
    elif choice == '2':
        recommendations.recommend_music()
    elif choice == '3':
        recommendations.recommend_game()
    elif choice == '4':
        jokes.tell_joke()
    elif choice == '5':
        stories.tell_fact()
    elif choice == '6':
        games.play_rps()
    elif choice == '7':
        games.play_guess_number()
    elif choice == '8':
        games.play_wheel_of_fortune()
    elif choice == '9':
        tictactoe.main()
    elif choice.lower() == 'exit':
        from termcolor import colored
        print(colored("👋 Спасибо за игру! До новых встреч!", "green", attrs=["bold"]))
        exit()
    else:
        from termcolor import colored
        print(colored("⚠️ Неверный выбор. Попробуйте снова.", "red"))


def main():
    loading_screen()
    while True:
        choice = show_main_menu()
        navigate(choice)
        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()