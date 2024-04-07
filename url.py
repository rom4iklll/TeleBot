'''
##################################

Статус кода - рабочий

Скрипт принимает ссылку на mail.ru
выгружает .pdf файл расписания

##################################
'''

import re
import requests
from TeleBot import link


def getUrl(link):

    # принимает ссылку на источник и обрабатывает
    response = requests.get(link)
    page_content = response.text

    re_pattern = r'dispatcher.*?weblink_get.*?url":"(.*?)"'
    match = re.search(re_pattern, page_content)

    if match:
        url = match.group(1)
        # получает /XXX/ГГГГГГГГГ по ссылке на источник
        parts = link.split('/')[-2:]
        # добавляет XXX и YYYYYYYY к ссылке
        url = f'{url}/{parts[0]}/{parts[1]}'
        return url

    return None


def getDownload():

    # скачивает файл по обработанной ссылке из функции getUrl(link)
    url = getUrl(link)
    response = requests.get(url)
    with open('Расписание.pdf', 'wb') as file:
        file.write(response.content)
        file.close()
    return
