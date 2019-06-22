# import requests
# from bs4 import BeautifulSoup as bs
#
#
# class Iterpals(object):
#     url = 'http://pythontutor.ru'
#
#     def login(self):
#         session = requests.Session()
#         url = 'http://pythontutor.ru/accounts/login/?next=/lessons/inout_and_arithmetic_operations/'
#         params = {'username': 'iluska',
#                   'password': 'jopahuyka'
#                   }
#         r = session.post(url, data=params)
#         if r.status_code == 200:
#             soup = bs(r.content, 'lxml')
#             print(soup)
#         else:
#             print('Error')
#
# Iterpals().login()

import requests

url = 'http://pythontutor.ru/accounts/login/'
session = requests.Session()
values = {'csrfmiddlewaretoken': 's5GySZ78nh8vZ5eNt7Lm60w4LgmGNBJPCNYWnPMNIuMKIWsjQwBnoHW7rLi9YkAa',
          'next': '/lessons/inout_and_arithmetic_operations/',
          'username': 'iluska',
          'password': 'jopahuyka'}

r = session.get(url, data=values)
if r.status_code == 200:
    print('OK')
print(r.text)


