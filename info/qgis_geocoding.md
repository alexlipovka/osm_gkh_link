# Идеи

Найден проект [https://geopy.readthedocs.io/en/stable/](https://geopy.readthedocs.io/en/stable/)

Протестировано в QGIS

Установить пакет `geopy` в OSGeo4W shell.

```shell
# Обновим pip
pip install --upgrade pip
# Установим geopy
pip install geopy
```

Открыть консоль Python

```python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="qgis")
location = geolocator.geocode("Ачинск, Лапенкова 13")

print(location)
13, проспект имени И.А. Лапенкова, 2-й Юго-Восточный микрорайон, Ачинск, городской округ Ачинск, Красноярский край, Сибирский федеральный округ, 662161, Россия
print(location.longitude, location.latitude)
90.48686398209158 56.2487153
```

```python
from geopy.geocoders import Nominatim
geolocator_ya = Yandex(user_agent = "qgis", api_key = "yandex_geocoding:api_key")
location = geolocator_ya.geocode("Ачинск, Лапенкова 13")

print(location)
проспект Лапенкова, 13, Ачинск, Красноярский край, Россия
print(location.longitude, location.latitude)
90.486894 56.248761
```

# Задачи

Геокодирование непривязанных адресов РеформыЖКХ.

## Города

Актуальные города на первую очередь:

- Ачинск
- Канск
- Зеленогорск

## Этапы

Этапы:
1. Выгрузка таблицы с проекта РеформаЖКХ
2. Выделение дубликатов по GUID
3. Подготовка маски для удаления дубликатов
4. Удаление дубликатов
5. Геокодирование таблицы по адресам

# Реализация

Геокодирование Яндрекс хорошо считывает ячейку полного адреса из таблицы РеформыЖКХ. Nominatim, наоборот, весьма требовательный к написанию — успешно справляется только с упрощенными запросами (просто название города, просто название улицы, номер дома), никаких дополнительных символов и лишних пробелов.

Яндекс API - до 1000 запросов в сутки.