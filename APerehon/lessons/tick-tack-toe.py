board = [i for i in range(1,10)]



def board_view():
    for i, elem in enumerate(board):
        if not i % 3 and i != 0:
            print(end='\n')
        print(elem, end='|')
    print()

def check(field):
    return True


def input_player():
    while True:
        try:
            field = int(input('Твой ход игрок->'))
        except:
            print('Вводи только числа')
        else:
            if field in range(1,10) and check(field):#должно выдавать True или False
                return field - 1
            print('Ввел не коректное число')
flag = True
tile = ['x','o']
while True:
    board_view()
    field = input_player()
    #field = int(input('Твой ход игрок->'))-1#нумерация в питоне с 0
    if flag:
        board[field] = tile[int(flag)]
    else:
        board[field] = tile[int(flag)]
    flag = not flag
#проверка на ввод
#функция проверки
#поставить флаг
#общение с пользователем