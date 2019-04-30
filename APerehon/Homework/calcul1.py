while 1:
    try:
        a = int(input('Введите число 1:'))
        b = int(input('Введите число 2:'))
        c = str(input('Действие:'))
    except ValueError:
        print('Вводить нужно числа!')
        continue

    try:
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
        elif c == 'exit':
            break
        else:
            print('Была допущена ошибка')
    except Exception as e:
        print(e)


print("All is okey")
