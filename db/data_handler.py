import logging
from typing import List

from db.database import conn_db
from db.models import *


def create_user(id_tg: int) -> Users:
    """
    Создает нового пользователя в базе данных.

    :param id_tg: ID Telegram пользователя.
    :return: Объект пользователя.
    """
    try:
        session, engine = conn_db()
        user = Users(id_tg=id_tg)
        session.add(user)
        session.commit()
        session.close()
        return user
    except Exception as e:
        logging.error(f"Error occurred while creating user: {e}")


def get_user_by_id_tg(id_tg: int) -> Users:
    """
    Получает пользователя по его ID Telegram из базы данных.

    :param id_tg: ID Telegram пользователя.
    :return: Объект пользователя.
    """
    try:
        session, engine = conn_db()
        user = session.query(Users).filter(Users.id_tg == id_tg).first()
        session.close()
        return user
    except Exception as e:
        logging.error(f"Error occurred while fetching user by ID: {e}")


def get_all_words() -> Words:
    """
    Получает все слова из базы данных.

    :return: Список всех слов в базе данных.
    """
    try:
        session, engine = conn_db()
        words = session.query(Words).all()
        session.close()
        return words
    except Exception as e:
        logging.error(f"Error occurred while fetching all words: {e}")


def get_all_words_studying(obj_user: Users) -> LearnedWordsUser:
    """
    Получает все слова, которые пользователь изучает.

    :param obj_user: Объект пользователя.
    :return: Список слов, которые пользователь изучает.
    """
    try:
        session, engine = conn_db()
        words_studying = session.query(LearnedWordsUser).filter(LearnedWordsUser.user_id == obj_user.id).all()
        session.close()
        return words_studying
    except Exception as e:
        logging.error(f"Error occurred while fetching all studying words: {e}")


def get_word_studying_user(word: str, obj_user: Users) -> LearnedWordsUser:
    """
    Получает слово, которое пользователь изучает.

    :param word: Слово для поиска.
    :param obj_user: Объект пользователя.
    :return: Слово, которое пользователь изучает.
    """
    try:
        session, engine = conn_db()
        word_studying_user = session.query(LearnedWordsUser).filter(
            LearnedWordsUser.word == word,
            LearnedWordsUser.user_id == obj_user.id
        ).all()
        session.close()
        return word_studying_user
    except Exception as e:
        logging.error(f"Error occurred while fetching studying word by user: {e}")


def save_words_studying_user(words: List[List[str]], obj_user: Users) -> List[LearnedWordsUser]:
    """
    Сохраняет слова, которые пользователь изучает.

    :param words: Список слов для сохранения.
    :param obj_user: Объект пользователя.
    :return: Список объектов слов, которые были сохранены.
    """
    try:
        session, engine = conn_db()

        obj_words = []
        for word in words:
            obj_words_studying_user = LearnedWordsUser(user_id=obj_user.id, word=word[0], translate=word[1])
            obj_words.append(obj_words_studying_user)
            session.add(obj_words_studying_user)

        session.commit()
        session.close()

        return obj_words
    except Exception as e:
        logging.error(f"Error occurred while saving studying words: {e}")


def del_words_studying_user(words: List[str], obj_user: Users) -> None:
    """
    Удаляет слова, которые пользователь изучает.

    :param words: Список слов для удаления.
    :param obj_user: Объект пользователя.
    """
    try:
        session, engine = conn_db()

        for word in words:
            session.query(LearnedWordsUser).filter_by(user_id=obj_user.id, word=word).delete()

        session.commit()
        session.close()
    except Exception as e:
        logging.error(f"Error occurred while deleting studying words: {e}")


def get_all_words_studied(obj_user: Users) -> WordsInLearningUser:
    """
    Получает все слова, которые пользователь изучил.

    :param obj_user: Объект пользователя.
    :return: Список слов, которые пользователь изучил.
    """
    try:
        session, engine = conn_db()
        words_studied = session.query(WordsInLearningUser).filter(WordsInLearningUser.user_id == obj_user.id).all()
        session.close()
        return words_studied
    except Exception as e:
        logging.error(f"Error occurred while fetching all studied words: {e}")


def save_word_studied_user(word: str, translate: str, obj_user: Users) -> None:
    """
    Сохраняет слово, которое пользователь изучил.

    :param word: Слово.
    :param translate: Перевод слова.
    :param obj_user: Объект пользователя.
    """
    try:
        session, engine = conn_db()

        obj_words_studying_user = WordsInLearningUser(user_id=obj_user.id, word=word, translate=translate)
        session.add(obj_words_studying_user)

        session.commit()
        session.close()
    except Exception as e:
        logging.error(f"Error occurred while saving studied word: {e}")


def del_words_studied_user(words: List[str], obj_user: Users) -> None:
    """
    Удаляет слова, которые пользователь изучил.

    :param words: Список слов для удаления.
    :param obj_user: Объект пользователя.
    """
    try:
        session, engine = conn_db()

        for word in words:
            session.query(WordsInLearningUser).filter_by(user_id=obj_user.id, word=word).delete()

        session.commit()
        session.close()
    except Exception as e:
        logging.error(f"Error occurred while deleting studied words: {e}")
