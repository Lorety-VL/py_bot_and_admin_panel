from .services import create_user, get_text


def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        user_id = message.from_user.id,
        create_user(user_id)
        text = "Привет! Я простой бот.\nУзнай что я могу по командой /help"
        bot.reply_to(message, text)

    @bot.message_handler(commands=['info'])
    def send_random_text(message):
        text = get_text()
        bot.reply_to(message, text.text if text else "Нет доступных текстов.")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        text = '''
        Это тестовый бот, который отправляет рандомный текст по команде: /info
        '''
        bot.reply_to(message, text)
