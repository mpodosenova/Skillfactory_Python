# Task: Модуль 5, Практическое задание "Крестики-нолики"

# Исходный вид игрового поля 3 на 3 (9 ячеек)
board = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'}

# Печать игрового поля
def print_board():
    print(f'{board[1]} {board[2]} {board[3]}\n{board[4]} {board[5]} {board[6]}\n{board[7]} {board[8]} {board[9]}')

# Список выигрышных комбинаций
win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# Функция хода: ставит крестик или нолик в выбранную ячейку и добавляет номер ячейки в список игрока
def move(player):
    while True:
        i = int(input('Введите номер ячейки от 1 до 9: '))
        if i < 0 or i > 9:
            print('Неверный номер ячейки')
        elif board[i] != '-':
            print('Эта ячейка уже занята')
        else:
            if player == 'X':
                board[i] = 'X'
                player_X.append(i)
            elif player == '0':
                board[i] = '0'
                player_0.append(i)
            break

# Функция проверки победителя
def check_win():
    win = None
    if len(player_X) >= 3 or len(player_0) >= 3:
        for i in range(8):
            if all([win_comb[i][0] in player_X, win_comb[i][1] in player_X, win_comb[i][2] in player_X]):
                win = 'X'
                print('Выиграл игрок Х')
            elif all([win_comb[i][0] in player_0, win_comb[i][1] in player_0, win_comb[i][2] in player_0]):
                win = '0'
                print('Выиграл игрок 0')
    return win

# Исходные данные игры
player_X = []
player_0 = []
game_count = 0
player = 'X'

# Игровой цикл
while True:
    if game_count >= 9:
        print('Ничья')
        break
    else:
        print(f'Игрок: {player}')
        game_count += 1
        move(player)
        print_board()
        win = check_win()
        if win:
            break
        player = 'X' if game_count % 2 == 0 else '0'
