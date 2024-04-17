import random
from typing import List

from telebot import types

from db.models import Words
from handlers.bot_constants import Command


def create_menu_keyboard():
    """
    Создает клавиатуру для основного меню бота.

    :return: Объект клавиатуры.
    """
    start_btn = types.KeyboardButton(Command.START)
    knowledge_base_btn = types.KeyboardButton(Command.KNOWLEDGE_BASE)
    studying_btn = types.KeyboardButton(Command.STUDYING)
    studyed_btn = types.KeyboardButton(Command.STUDYED)

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(start_btn, knowledge_base_btn, studying_btn, studyed_btn)
    return markup


def create_keyboard_with_words(obj_target_word: Words, others: List[str]):
    """
    Создает клавиатуру для ввода ответа на задание.

    :param obj_target_word: Слово, которое нужно перевести.
    :param others: Список других слов для выбора ответа.
    :return: Объект клавиатуры.
    """
    markup = types.ReplyKeyboardMarkup(row_width=2)

    target_word_btn = types.KeyboardButton(obj_target_word.translate)
    buttons = [target_word_btn]

    other_words_btns = [types.KeyboardButton(word) for word in others]
    buttons.extend(other_words_btns)
    random.shuffle(buttons)

    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            markup.add(buttons[i], buttons[i + 1])
        else:
            markup.add(buttons[i])

    return markup


def get_obj_next_or_default_word(bot, message, obj_words: Words, next_word: bool = False, back_word: bool = False):
    """
    Получает следующее или предыдущее слово из списка слов или возвращает первое слово.

    :param bot: Объект бота.
    :param message: Сообщение пользователя.
    :param obj_words: Список объектов слов.
    :param next_word: Флаг, указывающий на необходимость получения следующего слова.
    :param back_word: Флаг, указывающий на необходимость получения предыдущего слова.
    :return: Слово.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        target_word = data.get('target_word')
    words = [word.word for word in obj_words]

    word = obj_words[0]
    if target_word:
        if target_word in words:
            index = words.index(target_word)
            if next_word and index < len(words) - 1:
                word = obj_words[index + 1]
            elif back_word and index > 0:
                word = obj_words[index - 1]

    return word


def get_page_words_message(obj_words: List[str], page: int) -> str:
    """
    Формирует сообщение со словами для указанной страницы.

    :param obj_words: Список слов.
    :param page: Номер страницы.
    :return: Сообщение со словами на странице.
    """
    start_index = page * 10
    end_index = min(len(obj_words), (page + 1) * 10)
    page_words = obj_words[start_index:end_index]
    word_list = "\n".join([word.translate for word in page_words])
    return f"Слова на странице {page + 1}:\n{word_list}"


def check_translation_choice(bot, message):
    """
    Проверяет выбор пользователя при переводе слова и отправляет соответствующее сообщение.

    :param bot: Объект бота.
    :param message: Сообщение пользователя.
    """
    text = message.text

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        target_word = data['target_word']
        translate_word = data['translate_word']

    if text == translate_word:
        hint = f"{target_word} -> {translate_word}"
        hint_text = ["Отлично!❤", hint]

        hint = '\n'.join(hint_text)
    else:
        hint = f"Допущена ошибка! Попробуй ещё раз вспомнить слово 🇷🇺{translate_word}"

    bot.send_message(message.chat.id, hint)
