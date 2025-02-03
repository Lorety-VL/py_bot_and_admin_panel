from django.core.management.base import BaseCommand
import os
from telebot import TeleBot
from tg_bot.handlers import setup_handlers

class Command(BaseCommand):
    help = 'Запуск Telegram-бота'

    def handle(self, *args, **options):
        bot = TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])
        setup_handlers(bot)
        bot.polling(none_stop=True)