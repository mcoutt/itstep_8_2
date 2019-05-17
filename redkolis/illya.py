print('1')
t = True
if t: print('Its work!\n')

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

listOne = [2, 3, 4]
listTwo = [2 * i for i in listOne if i > 2]
print(listTwo)


def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
print(powersum(2, 10))
