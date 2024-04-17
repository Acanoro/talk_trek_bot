from handlers.views.manager.handle_manager_add_del_words import *
from handlers.views.manager.handle_manager_next_back_word import *
from handlers.views.manager.handle_manager_next_back_words import *

from handlers.views.handle_start import handle_start

from handlers.views.handle_menu import menu
from handlers.views.handle_knowledge_base import *
from handlers.views.handle_studied import handle_studied
from handlers.views.handle_studying import handle_studying
from handlers.views.handle_study import *

from handlers.views.manager.manager_message_text import manager_message_text


def register_handlers(bot):
    """
    Регистрирует обработчики сообщений для бота.

    :param bot: Объект бота.
    """
    # Команды
    bot.message_handler(commands=['start'])(lambda message: handle_start(bot, message))

    # Текстовые сообщения
    text_handlers = {
        'База знаний': handle_knowledge_base,
        'Меню': menu,
        'Изучать': handle_study,
        'Изучение': handle_studying,
        'Изучено': handle_studied,

        'Добавить слово ➕': handle_add_word,

        'Добавить в изучено': handle_add_word_study,

        'Назад ◀️': handle_back_word,
        'Дальше ▶️': handle_next_word,

        'Предыдущая страница': handle_prev_page,
        'Следующая страница': handle_next_page,

        'Добавить слова': handle_add_world,
        'Удалить слова': handle_del_world,
    }

    for text, handler in text_handlers.items():
        bot.message_handler(
            func=lambda message, text=text: message.text == text
        )(
            lambda message, handler=handler: handler(bot, message)
        )

    # Остальные текстовые сообщения
    bot.message_handler(
        func=lambda message: True, content_types=['text']
    )(
        lambda message: manager_message_text(bot, message)
    )
