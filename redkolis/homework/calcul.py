

while 1:
    try:
        a = int(input('Введие число 1 '))
        b = int(input('Введие число 2 '))
        c = str(input('Действие между числами '))
    except ValueError:
        print("Вводить нужно числа!")
        continue

    try:
        if c == '-':
            print(a - b)
        elif c == '+':
            print(a + b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
        elif c == 'exit':
            break
        else:
            print("Была допущена ошибка!")
    except ZeroDivisionError:
        print('Нельзя делить на 0!')
    except ValueError:
        print("Была допущена ошибка!")

print('Goodbye!')