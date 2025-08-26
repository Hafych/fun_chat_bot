import random
from colorama import init, Fore, Style
from termcolor import colored
import art
import emoji
from prettytable import PrettyTable

init(autoreset=True)


def drawBoard(board):
    """Отображает игровое поле с цветами и разделителями"""
    print("\n")
    for row in [7, 4, 1]:
        cells = []
        for i in range(3):
            cell = board[row + i]
            if cell == 'X':
                cells.append(Fore.RED + cell + Style.RESET_ALL)
            elif cell == 'O':
                cells.append(Fore.BLUE + cell + Style.RESET_ALL)
            else:
                cells.append(cell)
        print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
        if row != 1:
            print("———+———+———")
    print("\n")


def inputPlayerLetter():
    """Игрок выбирает X или O"""
    letter = ''
    while letter not in ['X', 'O']:
        print("Вы хотите играть за 🎌 'X' или за 🛶 'O'? (введите X или O)")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    """Определяет, кто ходит первым"""
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    """Ставит символ в клетку"""
    board[move] = letter


def isWinner(bo, le):
    """Проверяет, выиграл ли игрок"""
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or  # верх
        (bo[4] == le and bo[5] == le and bo[6] == le) or  # центр
        (bo[1] == le and bo[2] == le and bo[3] == le) or  # низ
        (bo[7] == le and bo[4] == le and bo[1] == le) or  # лево
        (bo[8] == le and bo[5] == le and bo[2] == le) or  # центр колонка
        (bo[9] == le and bo[6] == le and bo[3] == le) or  # право
        (bo[7] == le and bo[5] == le and bo[3] == le) or  # диагональ
        (bo[9] == le and bo[5] == le and bo[1] == le)     # диагональ
    )


def getBoardCopy(board):
    """Возвращает копию поля"""
    return board[:]


def isSpaceFree(board, move):
    """Проверяет, свободна ли клетка"""
    return board[move] == ' '


def getPlayerMove(board):
    """Получает ход игрока"""
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("Ваш ход! Введите клетку (1-9):")
        move = input()
        if not move.isdigit() or int(move) not in range(1, 10):
            print(Fore.YELLOW + "Введите число от 1 до 9!" + Style.RESET_ALL)
        elif not isSpaceFree(board, int(move)):
            print(Fore.RED + "Эта клетка занята!" + Style.RESET_ALL)
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    """Возвращает случайный допустимый ход"""
    possibleMoves = [i for i in movesList if isSpaceFree(board, i)]
    return random.choice(possibleMoves) if possibleMoves else None


def getComputerMove(board, computerLetter):
    """AI: логика хода компьютера"""
    playerLetter = 'O' if computerLetter == 'X' else 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """Проверяет, заполнено ли поле"""
    return all(cell != ' ' for cell in board[1:10])


def show_welcome():
    """Приветствие с ASCII-артом"""
    print(art.text2art("Tic Tac Toe", font="small"))
    print(colored(emoji.emojize("🎮 Добро пожаловать в Крестики-Нолики!"), "cyan", attrs=["bold"]))
    print(Fore.YELLOW + "Правила: ставьте X или O, чтобы собрать 3 в ряд." + Style.RESET_ALL)
    print("="*50)


def show_stats(player_wins, comp_wins, draws):
    """Показывает статистику"""
    table = PrettyTable()
    table.field_names = [colored("Игрок", "green"), colored("Компьютер", "red"), colored("Ничьи", "yellow")]
    table.add_row([player_wins, comp_wins, draws])
    table.align = "c"
    print(table)


def play_again():
    """Спросить, хочет ли игрок сыграть снова"""
    print("\n" + emoji.emojize("Хотите сыграть ещё раз? :thinking_face: (да/нет)"))
    return input().lower().startswith('д')


def main():
    show_welcome()

    player_wins = 0
    comp_wins = 0
    draws = 0

    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print(f"{turn} ходит первым.")

        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Человек':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print(colored(emoji.emojize("🎉 Ура! Вы выиграли! :trophy:"), "green", attrs=["bold"]))
                    player_wins += 1
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print(colored(emoji.emojize("🤝 Ничья! :handshake:"), "yellow", attrs=["bold"]))
                    draws += 1
                    gameIsPlaying = False
                else:
                    turn = 'Компьютер'

            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                print(f"Компьютер поставил {computerLetter} в клетку {move}...")

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print(colored(emoji.emojize("💀 Компьютер победил! Вы проиграли."), "red", attrs=["bold"]))
                    comp_wins += 1
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print(colored(emoji.emojize("🤝 Ничья! :handshake:"), "yellow", attrs=["bold"]))
                    draws += 1
                    gameIsPlaying = False
                else:
                    turn = 'Человек'

        show_stats(player_wins, comp_wins, draws)

        if not play_again():
            print(colored(emoji.emojize("Спасибо за игру! 👋"), "cyan"))
            break

if __name__ == "__main__":
    main()