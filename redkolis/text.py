from os import listdir


def readfile():
    file = open('text.txt', 'r')  # отображает содержимое в файле после изменения
    for line in file:
        print(line)
    file.close()


try:
    TF1 = True
    while TF1:
        TF = True
        print('Доступные файлы:')
        files = listdir(".")

        mytxt = list(filter(lambda x: x.endswith('.txt'), files))
        for i in mytxt:
            print(i.replace('.txt', ''))  # Выбор файла для работы
        choise = input('Выберите один из них либо введите "new" для создания нового:\n') + '.txt'
        if choise == 'new.txt':
            name = input('Введите название нового файла: ') + '.txt'
            file = open(name, 'a+')
            file.write(input("Введите то что хотите записать в файл: "))  # создание и работа с новым файлом
            file.write('\n')
            file.close()
        elif choise in mytxt:
            print('Ключевые фразы:\n', '"write" или "запись" - запись с новой строки\n',
                  '"clear" или "очистить" - удалить всё и записать с начала\n',
                  '"list" - для просмотра всех существующих файлов\n', '"close" - закрыть файл и выбрать другой\n',
                  '"exit" или "выход" - завершение работы\n')
            while TF:
                action: str = str(input('Выберите действие с файлом: '))  # выбор действия в файле

                if action == 'open' or action == 'открыть':
                    print("Вот содержимое файла:\n")
                    readfile()
                elif action == 'close':
                    break
                elif action == 'exit' or action == 'выход':
                    TF1 = False
                    break
                elif action == 'write' or action == 'запись':
                    try:
                        file = open('text.txt', 'a+')
                        file.write(input("Введите то что хотите записать в файл: "))  # записывает новую строку в файл
                        file.write('\n')
                    except Exception as e:
                        print(e)
                    finally:
                        file.close()
                        print("Вот содержимое файла после изменений:\n")
                        readfile()
                elif action == 'clear' or action == 'очистить':
                    file = open('text.txt', 'w+')
                    file.write(
                        input("Введите то что хотите записать в файл: "))  # записывает новую строку в очищенный файл
                    file.write('\n')
                    file.close()
                    print("Вот новое содержимое файла:\n")
                    readfile()

                else:
                    print('Wrong')
        else:
            print('Вводить можно только название существующего файла либо "new" для создания нового!')
except Exception as ex:
    print(ex)
print('Работа с файлами окончена!')
