class settings():
    """Класс с настройками
    """

    EXCEL_FILE_NAME: str  # Имя для EXCEL-файла для AVITO
    URL: str  # Базовый URL для парсинга
    DIRECTORY: str  # Директория для сохранения файлов
    ERROR: str  # Имя файла для вывода ссылок на необработанные объявления
    MIN: int  # Минимальное значение задержки
    MAX: int  # Максимальное значение задержки

    AVITO_PAGE_MARKER: str = "p"  # Параметр запроса для смены страницы

    CIAN_EXCEL_FILE: str = "offers.xlsx"  # Название EXCEL, скачанного с ЦИАН
    CIAN_EXCEL_LINK_HEADER: str = "Ссылка на объявление"  # Название столбца со ссылками
    CIAN_ID_HEADER: str = "ID  объявления"  # Название столбца с ID
    CIAN_LAST_UPDATE_COL_TITLE: str = "Обновлено"  # Добавляемый столбец с датой

    # XPATH Для ЦИАНА
    CIAN_IMAGE_XPATH = ".//div[@data-name='OfferGallery']//ul[@class='a10a3f92e9--container--Pf0cj']//img"
    CIAN_DATE_XPATH = ".//div[@data-testid='metadata-added-date']/span"
    CIAN_DOWNLOAD_EXCEL_BTN_XPATH = ".//div[@data-name='ButtonPrintExcelGroup']/button[position()=1]"
    CIAN_PDF_LINK_XPATH = ".//div[@data-name='Toolbar']//a"

    # XPATH Для парсинга пагинации с AVITO
    AVITO_NUM_PAGE_XPATH = ".//ul[@data-marker='pagination-button']/li[position()=last()-1]//span"

    # XPATH Для объявлений с AVITO
    AVITO_BTN_XPATH = ".//button[@data-marker='item-phone-button/card']"
    AVITO_MAIN_PIC_XPATH = ".//div[@data-marker='image-frame/image-wrapper']/img"
    AVITO_ON_EXTENDED_PIC_XPATH = ".//div[@data-marker='extended-image-preview/item']"
    AVITO_LINK_ITEMS_XPATH = ".//div[@data-marker='catalog-serp']/div[@data-marker='item']//a[@data-marker='item-title']"
    AVITO_ITEM_FOOTER = ".//div[@class='style-item-footer-Ufxh_']"
    AVITO_FOOTER_ID_XPATH = ".//span[@data-marker='item-view/item-id']"
    AVITO_FOOTER_PUBLISHED_ON_XPATH = ".//span[@data-marker='item-view/item-date']"
    AVITO_TITLE_XPATH = ".//h1[@data-marker='item-view/title-info']"
    AVITO_PRICE_XPATH = ".//span[@data-marker='item-view/item-price']"
    AVITO_SUBPRICE_XPATH = ".//div[@class='style-item-price-sub-price-_5RUD']/p/span"
    AVITO_SELLER_XPATH = ".//div[@data-marker='seller-info/name']//span"
    AVITO_SELLER_TYPE_XPATH = ".//div[@data-marker='seller-info/label']"
    AVITO_ADDRESS_XPATH = ".//div[@itemprop='address']/span"
    AVITO_GEOREF_XPATH = ".//span[@class='style-item-address-georeferences-item-TZsrp']/span[position()=last()]"
    AVITO_DESCR_XPATH = ".//div[@data-marker='item-view/item-description']/p"
    AVITO_USECASE_XPATH = ".//div[@data-marker='item-navigation']/div/span[position()=last()]/a/span"
    AVITO_INFO1_XPATH = ".//div[@data-marker='item-view/item-params']//li"
    AVITO_INFO2_XPATH = ".//ul[@class='style-item-params-list-vb1_H']/li"