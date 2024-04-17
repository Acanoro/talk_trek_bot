import os
import logging
from typing import List, Dict
from sqlalchemy.orm import Session

from db.models import *


def read_csv_data(file_path: str = None) -> List[Dict[str, str]]:
    """
    Чтение данных из CSV файла.

    :param file_path: Путь к CSV файлу. Если не указан, будет использоваться файл по умолчанию.
    :return: Список словарей с данными из CSV файла.
    """
    try:
        language_list = []

        if file_path is None:
            db_path = os.getcwd() + '\\db\\file\\base_words.csv'
        else:
            db_path = file_path

        with open(db_path, 'r', encoding='utf-8') as file:
            data = file.read().split()

            for word in data:
                language_list.append(
                    {
                        'en_word': word.split(',')[0],
                        'ru_word': word.split(',')[1],
                    }
                )

        return language_list
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: File '{file_path}' not found: {e}")
    except Exception as e:
        logging.error(f"Error reading file '{file_path}': {e}")


def fill_database(session: Session) -> None:
    """
    Заполнение базы данных словами из CSV файла.

    :param session: Сессия SQLAlchemy для взаимодействия с базой данных.
    """
    try:
        language_list = read_csv_data()
        words = [
            Words(
                word=lang_dict['ru_word'],
                translate=lang_dict['en_word'],
            ) for lang_dict in language_list
        ]

        session.add_all(words)
        session.commit()
    except Exception as e:
        logging.error(f"Error occurred while filling the database: {e}")
