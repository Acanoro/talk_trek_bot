import re

from db.data_handler import *
from handlers.utils.utils import *


def show_words_page(bot, message, chat_id: int, page: int):
    """
    Отображает страницу со словами для изучения.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.
        chat_id (int): Идентификатор чата.
        page (int): Номер страницы для отображения.

    Returns:
        None
    """
    obj_user = get_user_by_id_tg(id_tg=message.from_user.id)
    obj_words = get_all_words_studying(obj_user=obj_user)

    message_text = get_page_words_message(obj_words, page)

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    add_word_btn = types.KeyboardButton(Command.ADD_WORDS)
    del_word_btn = types.KeyboardButton(Command.DELETE_WORDS)
    next_page_btn = types.KeyboardButton(Command.NEXT_PAGE)
    back_page_btn = types.KeyboardButton(Command.BACK_PAGE)
    menu_btn = types.KeyboardButton(Command.MENU)

    markup.add(add_word_btn, del_word_btn)
    markup.add(back_page_btn, next_page_btn)
    markup.add(menu_btn)

    bot.send_message(chat_id, message_text, reply_markup=markup)


def handle_studying(bot, message):
    """
    Обрабатывает запрос пользователя на изучение слов.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['num_page'] = 0
        data['current_page'] = "Изучение"

    show_words_page(bot, message, message.chat.id, 0)


def add_world_studying(bot, message):
    """
    Добавляет слово для изучения.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    obj_user = get_user_by_id_tg(id_tg=message.from_user.id)
    obj_studying_words = get_all_words_studying(obj_user=obj_user)

    words_studying = [word.word for word in obj_studying_words]

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['action_on_page'] = ''

    words = message.text.split()

    word_list = []
    for i in words:
        # Проверяем, что строка соответствует формату "слово1-слово2"
        if re.match(r'^\w+-\w+$', i.strip()):
            word_list.append(i.strip().split("-"))
        else:
            bot.send_message(
                message.chat.id,
                'Не верно указаны слова. Нажмите на кнопку добавить еще раз и напишите слова.'
            )
            return

    if any(word_pair[0] in words_studying or word_pair[1] in words_studying for word_pair in word_list):
        bot.send_message(
            message.chat.id,
            'Одно или оба слова уже находятся в списке изучаемых слов.'
        )
        return

    save_words_studying_user(words=word_list, obj_user=obj_user)

    bot.send_message(message.chat.id, 'Слово успешно добавлено!')


def del_world_studying(bot, message):
    """
    Удаляет слово из изучения.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    obj_user = get_user_by_id_tg(id_tg=message.from_user.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['action_on_page'] = ''

    words = message.text.split()

    del_words_studying_user(words=words, obj_user=obj_user)
    bot.send_message(message.chat.id, 'Слово успешно удалено!')
