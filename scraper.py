import os
import re
import requests

import pandas as pd

from bs4 import BeautifulSoup
from csv import reader

ROOT_URL = 'https://minobrnauki.gov.ru'
LOCAL_JPG_DIR = 'data/jpg/'

person_names = []
names = []
person_ids = []
section_ids = []
links = []


def findExactSurname(word: str, string: str):
    return re.search(r'\b({0})\b'.format(word), string, flags=re.IGNORECASE)


def compareInitials(a: str, b: str):
    return a[:1].lower() == b[:1].lower()


print('working, please wait...')

with open('data/minobr_scrape_list.csv') as list:
    for row in reader(list):
        person_names.append(row[0])
        names.append(row[1])
        person_ids.append(row[4])
        section_ids.append(row[5])

df = pd.DataFrame(
    {
        'person_name': person_names[1:],
        'name': names[1:],
        'person_id': person_ids[1:],
        'section_id': section_ids[1:]
    }).drop_duplicates(subset=['person_name'])

source = requests.get(
    f'{ROOT_URL}/about/deps/'
)

deps = BeautifulSoup(source.text, features='html.parser')

for i in deps.find_all('a', {'class': 'department-item-link'}):
    links.append(i.attrs['href'])

for link in links:
    dep_source = requests.get(f'{ROOT_URL}{link}')
    dep = BeautifulSoup(dep_source.text, features='html.parser')
    for i in dep.find_all('a', {'class': 'administration-card-image'}):
        person_img = i.contents[1].attrs['src']
        person_name_web = i.find_next_sibling(
            'div', {'class': 'administration-card-body'}
        ).contents[1].text.split()
        if len(person_name_web) > 1:

            surname = person_name_web[0]
            name = person_name_web[1]

            for idx, row in df.iterrows():
                if findExactSurname(
                    surname, row['person_name']
                ) and compareInitials(
                    name, row['name']
                ):
                    if row['person_id'] != 'NULL':
                        img = f'{LOCAL_JPG_DIR}{row["person_id"]}.jpg'
                    else:
                        img = f'{LOCAL_JPG_DIR}section_{row["section_id"]}.jpg'
                    image = requests.get(f'{ROOT_URL}{person_img}').content
                    with open(img, 'wb') as file:
                        file.write(image)
                    df.drop(idx, inplace=True)

img_extensions = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
img_total = [fn for fn in os.listdir(path=LOCAL_JPG_DIR)
             if any(fn.endswith(ext) for ext in img_extensions)]

print(
    f'job done, {len(img_total)} files downloaded',
    f'to {os.path.abspath(LOCAL_JPG_DIR)}'
)
