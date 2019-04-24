#x = int (input())
#y = int (input())
#try:
#    res = x / y
#except ZeroDivisionError:
#    print ("Вы ввели 0")
#    res = 0
#print (res)

#try:
#   x = int (input ())
#except ValueError:
#    print ("Вы ввели не число")
#    x = 0
#print (x)

try:
    x = int(input())
except ValueError:
    print("вы ввели не число")
    x = 0
try:
    y = int(input())
except ValueError:
    print ("Вы ввели не число")
    y = 0
else:
    print("Все верно")
finally:
    print("выполнится 100%")
try:
    res = x / y
except ZeroDivisionError:
    print ("Вы ввели 0")
    res = 0
print (res)



