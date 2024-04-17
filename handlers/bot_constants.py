from telebot.handler_backends import State, StatesGroup


class Command:
    """
    Класс, содержащий команды бота.
    """
    MENU = 'Меню'
    START = 'Изучать'
    KNOWLEDGE_BASE = 'База знаний'
    STUDYING = 'Изучение'
    STUDYED = 'Изучено'

    ADD_WORD = 'Добавить слово ➕'
    ADD_WORD_STUDY = 'Добавить в изучено'

    NEXT = 'Дальше ▶️'
    BACK = 'Назад ◀️'

    NEXT_PAGE = 'Следующая страница'
    BACK_PAGE = 'Предыдущая страница'

    ADD_WORDS = 'Добавить слова'
    DELETE_WORDS = 'Удалить слова'


class MyStates(StatesGroup):
    """
    Группа состояний бота.
    """
    current_page_name = State()
    action_on_page = State()

    num_page_words = State()

    target_word = State()
    translate_word = State()
    another_words = State()

