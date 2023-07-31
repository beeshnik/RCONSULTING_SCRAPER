# RCONSULTING SCRAPER
Скрапер для прасинга авито и циана. Сохраняет скриншоты и данные в таблицу

# Установка
Для работы с программой установите интерпретатор языка Python <br/>
Например, отсюда: https://www.python.org/downloads/release/python-3114/ <br/>
<br/>
Выберите версию, которая подходит под вашу операционную систему <br/>
Если у вас Windows, то откройте вкладку "О компьютере" и посмотрите "Тип системы" <br/>
Там будет указана разрядность, она должна совпадать с разрядностью интерпретатора <br/>
Скачайте и установите интерпретатор <br/>

## Зависимости

Далее откройте командную строку (клавиши: <Win + R>) <br/>
Добавьте необходимые зависимости: <br/>
-- selenium <br/>
-- selenium_stealth <br/>
-- git+https://github.com/SergeyPirogov/webdriver_manager@master <br/>
-- pandas <br/>

Для этого используйте команду: pip install <название зависимости> <br/>

### При проблемах с webdriver:
https://stackoverflow.com/questions/63421086/modulenotfounderror-no-module-named-webdriver-manager-error-even-after-instal <br/>

## Настройки
Для настройки программы используйте файл settings.json <br/>
Описание параметров: <br/>
-- EXCEL_FILE_NAME: Название таблицы, в которую сохранить <br/>
-- URL: Ссылка на объявление <br/>
-- ERROR: Название файла для вывода ссылок на необработанные страницы (нежелательно менять) <br/>
-- AUTHOR: Автор программы <br/>
-- VERSION: Версия программы <br/>

## Результаты
Смотрите результаты в папке с названием формата: ГГГГ_ММ_ДД_ЧАС_МИНУТА_СЕКУНДА  <br/>
Например, 2023_07_31_17_14_24 для 31 июля 2023 (17:14)
