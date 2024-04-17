from handlers.views.handle_studied import del_world_studied
from handlers.views.handle_studying import *


def manager_message_text(bot, message):
    """
    Обрабатывает текстовые сообщения от пользователя и маршрутизирует их в соответствующие обработчики в зависимости от текущего состояния.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        current_page = data.get('current_page')
        action_on_page = data.get('action_on_page')

    if current_page == "Изучение":
        if action_on_page == "add_world":
            add_world_studying(bot, message)
        elif action_on_page == "del_world":
            del_world_studying(bot, message)
    elif current_page == "Изучено":
        if action_on_page == "del_world":
            del_world_studied(bot, message)
    elif current_page in [Command.START, Command.KNOWLEDGE_BASE]:
        check_translation_choice(bot, message)
    else:
        bot.send_message(message.chat.id, 'Неверная команда')
