print('1')
t = True
if t: print('Its work!\n')

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

listOne = [2, 3, 4]
listTwo = [2*i for i in listOne if i > 2]
print(listTwo)