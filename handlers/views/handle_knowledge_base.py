import random

from db.data_handler import *
from handlers.bot_constants import *
from handlers.utils.utils import *


def handle_knowledge_base(bot, message, next_word=False, back_word=False):
    """
    Обрабатывает процесс работы с базой знаний.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.
        next_word (bool): Флаг, указывающий, следует ли перейти к следующему слову.
        back_word (bool): Флаг, указывающий, следует ли вернуться к предыдущему слову.

    Returns:
        None
    """
    obj_words = get_all_words()
    obj_target_word = get_obj_next_or_default_word(
        bot=bot,
        message=message,
        obj_words=obj_words,
        next_word=next_word,
        back_word=back_word
    )

    others = [word.translate for word in random.sample(obj_words, 3)]
    markup = create_keyboard_with_words(obj_target_word, others)

    add_word_btn = types.KeyboardButton(Command.ADD_WORD)
    next_btn = types.KeyboardButton(Command.NEXT)
    back_btn = types.KeyboardButton(Command.BACK)
    menu_btn = types.KeyboardButton(Command.MENU)

    markup.add(add_word_btn)
    markup.row(back_btn, menu_btn, next_btn)

    greeting = f"Выбери перевод слова:\n🇷🇺 {obj_target_word.word}"
    bot.send_message(message.chat.id, greeting, reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.target_word, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['current_page'] = 'База знаний'
        data['target_word'] = obj_target_word.word
        data['translate_word'] = obj_target_word.translate
        data['other_words'] = others


def handle_add_word(bot, message):
    """
    Обрабатывает добавление слова в список изучаемых.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    user_id_tg = message.from_user.id

    obj_user = get_user_by_id_tg(user_id_tg)

    with bot.retrieve_data(user_id_tg, message.chat.id) as data:
        target_word = data['target_word']
        translate_word = data['translate_word']

    if not get_word_studying_user(word=target_word, obj_user=obj_user):
        save_words_studying_user(words=[[target_word, translate_word]], obj_user=obj_user)
        bot.send_message(message.chat.id, f"слово ({target_word}) добавлено")
    else:
        bot.send_message(message.chat.id, f"слово ({target_word}) уже добавлено")
