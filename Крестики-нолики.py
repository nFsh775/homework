board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_board():
    """Выводит текущее состояние игрового поля."""
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')* 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print (('_' * 3 + '|')* 3)


def step(index, char):
    """Выполняем ход"""
    # Проверяем правильно ли введен индекс и занята ли ячейка, которую выбрал игрок
    if (index < 1 or index > 9 or board[index - 1] in ('X', 'O')):
        return False

    # Если правильно, то присваиваем ячейке значение 'X' или 'O'
    board[index - 1] = char
    return True


def check_win():
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), #горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8), #вертикальные линии
        (0, 4, 8), (2, 4, 6), #диагональные линии
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def process_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    move_number = 1
    print_board()
    while (move_number < 10) and (check_win() == False):
        input_index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')

        if (input_index == '0'):
            break

        if step((int(input_index)), current_player):
            print('Ход выполнен')

            print_board()
            move_number += 1

            #смена игрока
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Номер неверный. Повторите')

    if (move_number == 10):
        print('Игра окончена. Ничья!')
    else:
        print('Выиграл ' + check_win())

print('Добро пожаловать в игру "Крестики-нолики"')
process_game()
