# chaplinskiy/wsf_scraper
Тестовое задание для [Web Security Fellowship](https://wsf.digsec.org/).

## Что это тут у нас:
Скрипт-парсер для скачивания фотографий работников [департаментов МинОбрНауки РФ](minobrnauki.gov.ru/about/deps/).

### Как пользоваться:

Склонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/chaplinskiy/wsf_scraper.git
```

```bash
cd wsf_scraper
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Запустить скрипт:

```bash
python3 scraper.py
```

Фотографии скачаются в папку `data/jpg`.

### Дисклеймер:

Работники приходят, уходят и перемещаются по карьерной лестнице туда-сюда, поэтому нелишним будет проверить некоторых персонажей вручную (например, `person_id = 378702` и `person_id = 386075`).

### Другие проекты автора:
https://github.com/chaplinskiy/
