# О проекте

Цель данного проекта — обеспечить оперативное соединение данных проекта [OpenStreetMap](https://www.openstreetmap.org/) и портала [РеформаЖКХ](https://www.reformagkh.ru/).

Предпринята попытка создания универсального выражения для адресных полей выгрузки OSM и РеформыЖКХ, через которые можно выполнить табличное пересечение.

# Инструкция

## Вариант 1

1. Клонировать проект, либо скопировать файлы `osm_building.qml` и `gkh_building.qml`.
2. Запустить QGIS и скачать слой застройки с помощью плагина [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) по тегу `building`.
3. Загрузить таблицу с реестром домов с портала [РеформаЖКХ](https://www.reformagkh.ru/) из раздела [Открытые данные](https://www.reformagkh.ru/opendata?cids=house_management&page=1&pageSize=10).
4. Импортировать таблицу в QGIS.
5. Загрузить стиль полей для слоя застройки (`osm_building.qml`) и стиль полей (`gkh_building.qml`) для реестра домов.
6. Настроить связь через новое виртуальное поле `address_link`.

## Вариант 2

1. Установить плагин [`QGIS Resource Sharing`](https://qgis-contribution.github.io/QGIS-ResourceSharing/).
2. Добавить данный репозиторий (Меню «Интернет → Resource Sharing → Settings → Add repository...»).
3. Установить коллекцию `OSM-ReformsGKH` и открыть папку со стилями кнопкой «Open folder».
4. Запустить QGIS и скачать слой застройки с помощью плагина [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) по тегу `building`.
5. Загрузить таблицу с реестром домов с портала [РеформаЖКХ](https://www.reformagkh.ru/) из раздела [Открытые данные](https://www.reformagkh.ru/opendata?cids=house_management&page=1&pageSize=10).
6. Импортировать таблицу в QGIS.
7. Загрузить стиль полей для слоя застройки (`osm_building.qml`) и стиль полей (`gkh_building.qml`) для реестра домов.
8. Настроить связь через новое виртуальное поле `address_link`. 

# Область применения

На данный момент (2021.09.23) настроена связка только на примере Красноярска. В результате образуется 5283 связи.