import json
import os
from datetime import datetime
from pathlib import Path

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
            settings.EXCEL_FILE_NAME = data["EXCEL_FILE_NAME"] + ".xlsx"
            settings.URL = data["URL"]
            settings.ERROR = data["ERROR"]
            settings.MIN = data["MIN"]
            settings.MAX = data["MAX"]
            settings.DIRECTORY = data["DIRECTORY"]
            if settings.MIN >= settings.MAX:
                raise RuntimeError("Максимум должен быть строго больше минимума!")
            Utils.check_directory()

    @staticmethod
    def check_directory():
        """Подготавливает директорию для работы
        Если создать невозможно, то создает стандартную, используя системное время
        """

        Path(f'{settings.DIRECTORY}\\{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}').mkdir()

    @staticmethod
    def get_path(filename: str) -> str:
        """Конкатенирует имя файла со стандартной директорией из настроек

        Args:
            filename (str): название файла (с расширением)

        Returns:
            str: полный путь до файла
        """

        return f"{settings.DIRECTORY}/{filename}"