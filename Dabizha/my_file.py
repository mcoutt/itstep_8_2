#Получаем 4 переменные:

    #Номер накладной
    #Дата выписки
    #Дата регистрации
    #Сума НДС

#Вычисляем количество дней прострочки:

    #Если дата выписки с 1 по 15 число, то дата регистрации должна быть до последнего дня текущего месяца
        #считаем количество дней между последним днем месяца и датой регистрации

    #Если дата выписки с 16 по последний день месяца, то дата регистрации должна быть до 15 числа следующего месяца
        #считаем количество дней между 15 числом следующего месяца и датой регистрации

#Если количество дней прострочки <= 0 то штрафа нет
    #Если количество дней прострочки от 1 до 15 то умножаем Суму НДС на 0,1
    #Если количество дней прострочки от 16 до 30 то умножаем Суму НДС на 0,2
    #Если количество дней прострочки от 31 до 60 то умножаем Суму НДС на 0,3
    #Если количество дней прострочки > 60 то умножаем Суму НДС на 0,4

#Выводим:
    #Номер накладной
    #Дата выписки
    #Дата регистрации
    #Сума НДС
    #Количество дней прострочки
    #Суму штрафа