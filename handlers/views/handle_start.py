from db.data_handler import *
from handlers.utils.utils import create_menu_keyboard


def handle_start(bot, message):
    """
    Обрабатывает начало диалога с пользователем.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    chat_id = message.chat.id

    greeting_text = """
Главное меню

В главном меню вы увидите 4 кнопки:

Изучать: здесь вы будете учить слова из вашего списка "Изучение".
База знаний: предоставляет возможность выбрать слова для изучения и проверки знаний.
Изучение: просмотр слов, которые вы изучаете в данный момент. Здесь вы можете пополнить список или удалить слова.
Изучено: просмотр слов, которые вы уже выучили. Вы также можете удалять слова из этого раздела.
    """

    if not get_user_by_id_tg(message.from_user.id):
        bot.send_message(chat_id, f"Привет {message.chat.username}!\n{greeting_text}")
        create_user(message.chat.id)
    else:
        bot.send_message(chat_id, f"С возвращением {message.chat.username}!")

    bot.set_state(message.from_user.id, None, message.chat.id)

    markup = create_menu_keyboard()
    bot.send_message(chat_id, "Меню", reply_markup=markup)
