try:
    i = int(input('введите число: '))
    next_number = int(input('введите другое число: '))
    kind = input('введите вид операции: ')
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
        print("Наш результат с целым числом: ", i // next_number)
except ValueError:
    print('Value Error, please enter other')
except ZeroDivisionError:
    print('do not divide on zero')
print('ВЫ УСПЕШНО ЗАКОНЧИЛИ ОПЕРАЦИЮ')