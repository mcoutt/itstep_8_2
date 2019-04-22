try:
    TF = True
    print('Добро пожаловать в блокнот!\n', 'Ключевые фразы:\n', '"exit" или "выход" - завершение работы в блокноте\n',
          '"open" или "открыть" - просмотр содержимого\n', '"write" или "запись" - запись с новой строки\n', )
    while TF:
        action = str(input('Выберите действие с файлом: '))  # выбор действия в файле

        if action == 'open' or 'открыть':
            file = open('text.txt', 'r')  # отображает содержимое в файле
            for line in file:
                print(line)
            file.close()
        elif action == 'exit' or 'выход':
            TF = False
            continue
        elif action == 'write' or 'запись':
            try:
                file = open('text.txt', 'a+')
                file.write(input("Введите то что хотите записать в файл: "))  # записывает новую строку в файл
                file.write('\n')

            except Exception as e:
                print(e)
            finally:
                file.close()
        else:
            print('Wrong')
except Exception as ex:
    print(ex)
print('Работа с файлом окончена!')
