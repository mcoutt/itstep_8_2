from os import listdir


def readfile():
    file = open(choise, 'r')  # отображает содержимое в файле после изменения
    for line in file:
        print(line)
    file.close()


try:
    TF1 = True
    while TF1:
        TF = True
        print('Доступные файлы:')
        files = listdir(".")    # отображение существующих файлов

        mytxt = list(filter(lambda x: x.endswith('.txt'), files))
        for i in mytxt:
            print(i.replace('.txt', ''))  # Выбор файла для работы
        choise = input('Выберите один из них либо введите "new" для создания нового:\n') + '.txt'
        if choise == 'new.txt':  # создание нового файла
            name = input('Введите название нового файла: ') + '.txt'
            while 1:
                if name == 'new.txt':  # убираю конфликты в названиях
                    name = input('Введите другое название для файла: ') + '.txt'
                elif name in mytxt:
                    name = input('Такой файл уже существует, введите другое название для файла: ') + '.txt'
                else:
                    print('Файл с названием "{0}" успешно создан'.format(name.replace('.txt', '')))
                    file = open(name, 'a+')
                    file.write(' ')
                    file.close()
                    break
        elif choise in mytxt:  # работа с существующим файлом
            print('Ключевые фразы:\n', '"write" или "запись" - запись с новой строки\n',
                  '"clear" или "очистить" - удалить всё и записать с начала\n',
                  '"close" - закрыть файл и выбрать другой\n',
                  '"exit" или "выход" - завершение работы\n')
            print("Вот содержимое файла:\n")
            readfile()
            while TF:
                try:
                    action: str = str(input('Выберите действие с файлом: '))  # выбор действия в файле
                    if action == 'close':
                        TF = False
                    elif action == 'exit' or action == 'выход':
                        TF1 = False  # конец работы с файлом
                        TF = False
                    elif action == 'write' or action == 'запись':
                        file = open(choise, 'a+')
                        file.write(input("Введите то что хотите записать в файл: "))  # записывает новую строку в файл
                        file.write('\n')
                        file.close()
                        print("Вот содержимое файла после изменений:\n")
                        readfile()
                    elif action == 'clear' or action == 'очистить':
                        file = open(choise, 'w+')  # выход с файла
                        file.write(
                            input("Введите то что хотите записать в файл: "))
                        file.write('\n')  # записывает новую строку в очищенный файл
                        file.close()
                        print("Вот новое содержимое файла:\n")
                        readfile()
                    else:
                        print('Wrong')
                        continue
                except Exception as e:
                    print(e)
        else:
            print('Вводить можно только название существующего файла либо "new" для создания нового!')
except Exception as ex:
    print(ex)
print('Работа с файлами окончена!')
