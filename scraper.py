import os
import re
import requests

import pandas as pd

from bs4 import BeautifulSoup
from csv import reader

ROOT_URL = 'https://minobrnauki.gov.ru'
LOCAL_JPG_DIR = 'data/jpg/'

person_name = []
person_id = []
section_id = []
links = []


def findExactSurname(word, string):
    return re.search(r'\b({0})\b'.format(word), string, flags=re.IGNORECASE)


with open('data/minobr_scrape_list.csv') as list:
    for row in reader(list):
        person_name.append(row[0])
        person_id.append(row[4])
        section_id.append(row[5])

df = pd.DataFrame(
    {
        'person_name': person_name[1:],
        'person_id': person_id[1:],
        'section_id': section_id[1:]
    }).drop_duplicates(subset=['person_name'])

source = requests.get(
    f'{ROOT_URL}/about/deps/'
)

deps = BeautifulSoup(source.text, features='html.parser')

for i in deps.find_all('a', {'class': 'department-item-link'}):
    links.append(i.attrs['href'])

print('working, please wait...')

for link in links:
    dep_source = requests.get(f'{ROOT_URL}{link}')
    dep = BeautifulSoup(dep_source.text, features='html.parser')
    for i in dep.find_all('a', {'class': 'administration-card-image'}):
        person_img = i.contents[1].attrs['src']
        person_name_web = i.find_next_sibling(
            'div', {'class': 'administration-card-body'}
        ).contents[1].text
        if len(person_name_web) > 1:
            surname = person_name_web.split()[0]
            for idx, row in df.iterrows():
                if findExactSurname(surname, row['person_name']):
                    if row['person_id'] != 'NULL':
                        pic = f'{LOCAL_JPG_DIR}{row["person_id"]}.jpg'
                    else:
                        pic = f'{LOCAL_JPG_DIR}section_{row["section_id"]}.jpg'
                    image = requests.get(f'{ROOT_URL}{person_img}').content
                    with open(pic, 'wb') as file:
                        file.write(image)

print(
    f'job done, {len(os.listdir(path=LOCAL_JPG_DIR))} files downloaded',
    f'to {os.path.abspath(LOCAL_JPG_DIR)}'
)
