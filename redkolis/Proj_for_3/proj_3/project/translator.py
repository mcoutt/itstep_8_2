import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
base_url = 'https://translate.google.com/?hl=ru#view=home&op=translate&sl=en&tl=ru'


def translate(base_url, headers):
    session = requests.Session()
    request = session.post(base_url, headers=headers)
    if request.status_code == 200:
        # soup = bs(request.content, 'lxml')
        print('Ok')
    else:
        print('ERROR')


translate(base_url, headers)
