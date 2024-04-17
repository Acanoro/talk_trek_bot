from db.data_handler import *
from handlers.utils.utils import *


def show_words_page(bot, message, chat_id: int, page: int):
    """
    Отображает страницу со словами, которые пользователь уже изучил.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.
        chat_id (int): Идентификатор чата.
        page (int): Номер страницы для отображения.

    Returns:
        None
    """
    obj_user = get_user_by_id_tg(id_tg=message.from_user.id)
    obj_words = get_all_words_studied(obj_user=obj_user)

    message_text = get_page_words_message(obj_words, page)

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    del_word_btn = types.KeyboardButton(Command.DELETE_WORDS)
    next_page_btn = types.KeyboardButton(Command.NEXT_PAGE)
    back_page_btn = types.KeyboardButton(Command.BACK_PAGE)
    menu_btn = types.KeyboardButton(Command.MENU)

    markup.add(del_word_btn)
    markup.add(back_page_btn, next_page_btn)
    markup.add(menu_btn)

    bot.send_message(chat_id, message_text, reply_markup=markup)


def handle_studied(bot, message):
    """
    Обрабатывает запрос пользователя на просмотр изученных слов.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['num_page'] = 0
        data['current_page'] = "Изучено"

    show_words_page(bot, message, message.chat.id, 0)


def del_world_studied(bot, message):
    """
    Обрабатывает удаление слова из изученных.

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

    del_words_studied_user(words=words, obj_user=obj_user)

    bot.send_message(message.chat.id, 'Слово успешно удалено!')
