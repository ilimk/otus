import os

import requests
from bs4 import BeautifulSoup
from os import path

def http_request(http):
    response = requests.get(http)
    soup = BeautifulSoup(response.content, 'html.parser')
    href_tags = soup.find_all(href=True)
    true_address = []
    for i in href_tags:
        hrefs = i.get('href')

        if 'stackoverflow' not in hrefs[0:hrefs.find('/', 8, len(hrefs))] and (hrefs[0:hrefs.find('/')] == 'http:' or hrefs[0:hrefs.find('/')] == 'https:'):
            true_address.append(hrefs)

    return true_address


address = http_request('https://stackoverflow.com/')

a = input('Выберите вариант парсинга, 1-Показать в консоли, 2-Залить все в файл :')

if a == '1':
    for i in address:
        print('первые адреса', i)
        for j in http_request(i):
            print('вложенные адреса', j)
elif a == '2':
    print('Вы выбрали вариант в файле')
    if path.exists('stackoverflowFiles.txt') is True:
        os.remove('stackoverflowFiles.txt')

    with open('stackoverflowFiles.txt', 'w') as file:
        for i in address:
            file.write(i)
            for j in http_request(i):
                file.write(j)
