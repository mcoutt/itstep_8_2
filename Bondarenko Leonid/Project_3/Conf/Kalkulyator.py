try:
    i = int(input('Введите число и нажмите Enter: '))
    next_number = int(input('Введите другое число и нажмите Enter: '))
    kind = input('Введите вид операции и нажмите Enter: *, /, +, -, //, %: ')
    result = i, kind, next_number
    if kind == '+':
        print("Наш результат со сложением: ", i + next_number)
    elif kind == '-':
        print("Наш результат с вычитанием: ", i - next_number)
    elif kind == '*':
        print("Наш результат с умножением: ", i * next_number)
    elif kind == '/':
        print("Наш результат с делением: ", i / next_number)
    elif kind == '**':
        print("Наш результат с возведением в степень: ", i ** next_number)
    elif kind == '//':
        print("Наш результат - целая часть от частного: ", i // next_number)
    elif kind == '%':
        print("Наш результат - остаток от деления: ", i % next_number)
except ValueError:
    print('Value Error, please enter other')
except ZeroDivisionError:
    print('do not divide on zero')
print('ВЫ успешно закончили операцию')