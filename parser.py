'''
##################################

Статус кода - рабочий

Скрипт получает ссылку на mail.ru

##################################
'''


import requests
from bs4 import BeautifulSoup as bs


def getLink():

    # парсинг сайта колледжа
    link_college = 'http://eetk.ru/78-2/82-2/88-2/'
    response = requests.get(link_college).text
    soup = bs(response, 'lxml')

    # парсинг расписаний курсов
    link = soup.find('div', id='main')
    link = link.find('table', id='wp-table-reloaded-id-58-no-1')
    # В перспективе добавить выбор курса
    link = link.find_all('td')[1]
    link = [link.get('href') for link in link.find_all('a')]
    link = link[0]
    return link
