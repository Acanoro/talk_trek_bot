from db.data_handler import *
from handlers.views.handle_studying import show_words_page as show_words_page_studying
from handlers.views.handle_studied import show_words_page as show_words_page_studied


def handle_prev_page(bot, message):
    """
    Обрабатывает команду перехода к предыдущей странице.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        current_page = data.get('current_page')
        num_page = data['num_page']
        new_num_page = num_page - 1
        data['num_page'] = new_num_page

    if current_page == "Изучение":
        show_words_page_studying(bot, message, message.chat.id, new_num_page)
    elif current_page == "Изучено":
        show_words_page_studied(bot, message, message.chat.id, new_num_page)


def handle_next_page(bot, message):
    """
    Обрабатывает команду перехода к следующей странице.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        current_page = data.get('current_page')
        num_page = data['num_page']
        new_num_page = num_page + 1
        data['num_page'] = new_num_page

    if current_page == "Изучение":
        show_words_page_studying(bot, message, message.chat.id, new_num_page)
    elif current_page == "Изучено":
        show_words_page_studied(bot, message, message.chat.id, new_num_page)
