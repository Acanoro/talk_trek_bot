import telebot
from dotenv import dotenv_values
from telebot import StateMemoryStorage
import logging

from db.database import conn_db
from handlers.register_handlers import register_handlers
from logger_config import setup_logging

secrets = dotenv_values(".env")


def main():
    """
    Основная функция запуска бота.
    """
    try:
        setup_logging()
        conn_db(create_tables_flag=True, fill_database_flag=True)
        state_storage = StateMemoryStorage()
        bot = telebot.TeleBot(secrets['TOKEN'], state_storage=state_storage)
        register_handlers(bot)
        bot.polling()
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    logging.info('Starting the bot...')
    main()



