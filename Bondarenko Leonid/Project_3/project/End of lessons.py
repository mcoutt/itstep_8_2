#В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут,
# после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
#Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
#Выведите два целых числа: время окончания урока в часах и минутах.

print('Введите номер урока, нажите Enter: ')

x = int(input())
if x ==1:
    print('9' ' ' '45')
if x ==2:
    print('10' ' ' '35')
if x == 3:
    print('11' ' ' '35')
if x == 4:
    print('12' ' ' '25')
if x == 5:
    print('13' ' ' '25')
if x == 6:
    print('14' ' ' '15')
if x == 7:
    print('15' ' ' '15')
if x == 8:
    print('16' ' ' '5')
if x == 9:
    print('17' ' ' '5')
if x == 10:
    print('17' ' ' '55')
print('Окончание урока')
