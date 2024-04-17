def handle_add_world(bot, message):
    """
    Обрабатывает команду добавления слова.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['action_on_page'] = 'add_world'

    instructions_adding_words = """
Пример добавления слов:

мир-world
яблоко-apple

Важно писать только нижним регистром. Первое слово на русском, второе на английском. Пробелов не должно быть. Новые слова пишите с новой строки.
    """

    bot.send_message(message.chat.id, f"добавьте слова\n{instructions_adding_words}")


def handle_del_world(bot, message):
    """
    Обрабатывает команду удаления слова.

    Args:
        bot: Экземпляр бота.
        message: Сообщение от пользователя.

    Returns:
        None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['action_on_page'] = 'del_world'

        instructions_del_words = """
    Пример удаления слов:

    мир
    яблоко

    Указывайте только первое слово на русском языке. Новые слова пишите с новой строки.
        """

    bot.send_message(message.chat.id, f"удалите слова\n{instructions_del_words}")
