
dic = {
    'Ivan': 'г. Турунтаево, ул. Новоселки 4-я, дом 97, квартира 242',
    'Andrew': 'г. Болхов, ул. Северная 2-я Линия, дом 8, квартира 262',
    'Nick': 'г. Климово, ул. Прядильная 3-я, дом 13, квартира 119'
}
action = input('Выберите действие\n')

if action == 'view name':
    for i in dic.keys():
        print(i, end='\n')
elif action == 'view address':
    for i in dic.values():
        print(i, end='\n')
