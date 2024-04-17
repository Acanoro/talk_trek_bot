from handlers.views.handle_knowledge_base import handle_knowledge_base
from handlers.views.handle_study import handle_study


def handle_back_word(bot, message):
    """
    Обрабатывает команду перехода к предыдущему слову.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        current_page = data['current_page']

    if current_page == "База знаний":
        handle_knowledge_base(bot, message, back_word=True)
    elif current_page == "Изучать":
        handle_study(bot, message, back_word=True)


def handle_next_word(bot, message):
    """
    Обрабатывает команду перехода к следующему слову.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        current_page = data['current_page']

    if current_page == "База знаний":
        handle_knowledge_base(bot, message, next_word=True)
    elif current_page == "Изучать":
        handle_study(bot, message, next_word=True)
