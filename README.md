# chaplinskiy/wsf_scraper
Тестовое задание для [Web Security Fellowship](https://wsf.digsec.org/).

## Что это тут у нас:
Скрипт-парсер для скачивания фотографий работников [департаментов МинОбрНауки РФ](https://minobrnauki.gov.ru/about/deps/).

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

Установить зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

Запустить скрипт:

```bash
python3 scraper.py
```

Фотографии скачаются в папку `data/jpg/`.

### Дисклеймер:

Однофамильцы фильтруются только по первому инициалу (т.е. по имени).

Если на сайте МинОбра вместо реальной фотографии сотрудника висит плейсхолдер – он тоже скачается. Таких случаев будет немного, их можно обработать вручную.

### Другие проекты автора:
https://github.com/chaplinskiy/
