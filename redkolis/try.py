def start():
    print('Приветствую вас в игре "Крестики-Нолики"!\nверсия_1.0\n')
    print('Поля номеруются таким образом:')
    print('\t\t|', end='')
    for i in range(1, 10):
        print(i, end='|')

        fields.append(i)
        if len(fields) % 3 == 0 and len(fields) != 9:
            print('\n\t\t' + '|', end='')
        elif len(fields) == 9:
            print()
    print("Для хода введите номер поля на которое хотите походить")
    answer = first_question()
    print("\n\tИгра Началась!\n")
    return answer


def start_new_game():
    for i in range(1, 10):
        fields.append(i)
    answer = first_question()
    print("\n\tИгра Началась!\n")
    return answer


def new_frame():
    a = 0
    print('\t\t|', end='')
    for i in fields:
        a += 1
        if i == 'X' or i == 'O':
            print(i, end='|')
        else:
            print(" ", end='|')
        if a % 3 == 0 and a != 9:
            print('\n\t\t' + '|', end='')
        elif a == 9:
            print()


def move():
    while True:
        try:
            choice = int(input('\nВыберите поле для хода --> '))
            print()
        except:
            print("Вводите числа от 1 до 9!")
        else:
            if choice in range(1, 10) and choice in fields:
                return choice - 1
            else:
                print('Поле заполнено!')


def winner():
    win_ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for w in win_ways:
        if fields[w[0]] == fields[w[1]] == fields[w[2]]:
            print(f'\n\nПобедил игрок играющий за "{fields[w[0]]}"!\n')
            return False
        else:
            draw = True
            for i in fields:
                if i in range(1, 10):
                    draw = False
            if draw:
                print('\n\t\tНичья!\n')
                return False
    return True


def computer_move():
    mov = 0
    best_move = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    while True:
        choice = best_move[mov]
        if fields[choice] not in tile:
            print(f'\nЯ выбираю поле "{choice + 1}"\n')
            return choice
        else:
            mov += 1


def first_question():
    while True:
        question = str(input('\nХотели бы вы сделать первый ход?(y/n)--> '))
        if question.lower() == 'y' or question.lower() == 'n':
            if question == 'y':
                return True
            else:
                return False
        else:
            print('Введите пожалуйста "y" для подтверждения или "n" для отказа')


def last_question():
    while True:
        question = str(input('Хотели бы вы сыграть ещё?(y/n)--> '))
        # print()
        if question.lower() == 'y' or question.lower() == 'n':
            if question == 'y':
                return True, 2
            else:
                print('\n\tСпасибо за игру!')
                return False, 1
        else:
            print('Введите пожалуйста "y" для подтверждения или "n" для отказа')


new_game, game = True, 1
while new_game:
    fields = []
    tile = ['O', 'X']
    if game > 1:
        turn = start_new_game()
    else:
        turn = start()
    flag = True
    new_frame()
    end = winner()
    while end:
        try:
            if turn:
                choice = move()
            else:
                choice = computer_move()
            if flag:
                fields[choice] = tile[int(flag)]
            else:
                fields[choice] = tile[int(flag)]
        except IndexError:
            pass
        new_frame()
        end = winner()
        flag = not flag
        turn = not turn
    new_game, game = last_question()
