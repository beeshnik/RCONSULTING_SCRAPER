import json
import os
from datetime import datetime

from settings.settings import settings

class Utils():
    """Вспомогательный класс
    """

    @staticmethod
    def load_settings():
        """Устанавливает настройки из файла settings.json
        """
        
        with open('settings.json') as json_file:
            data = json.load(json_file)
            settings.EXCEL_FILE_NAME = data["EXCEL_FILE_NAME"]
            settings.URL = data["URL"]
            settings.ERROR = data["ERROR"]
            settings.MIN = data["MIN"]
            settings.MAX = data["MAX"]
            Utils.check_directory()
    
    @staticmethod
    def check_directory():
        """Подготавливает директорию для работы
        Если создать невозможно, то создает стандартную, используя системное время
        """

        settings.DIRECTORY = f"{os.getcwd()}\{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        os.makedirs(settings.DIRECTORY)

    @staticmethod
    def get_path(filename: str) -> str:
        """Конкатенирует имя файла со стандартной директорией из настроек

        Args:
            filename (str): название файла (с расширением)

        Returns:
            str: полный путь до файла
        """
        
        return f"{settings.DIRECTORY}/{filename}"