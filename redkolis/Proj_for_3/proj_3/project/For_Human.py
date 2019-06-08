import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

base_url = 'https://kiev.hh.ua/search/vacancy?area=5&clusters=true&currency_code=UAH&enable_snippets=true&search_period=3&text=python&page=0'


def hh_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            content = text1 + ' ' + text2
            jobs.append({
                'Название должности': title,
                'Ссылка': href,
                'Название компании': company,
                'Описание': content
            })
        for i in jobs:
            print(i, end='\n')

    else:
        print('ERROR')


hh_parse(base_url, headers)
