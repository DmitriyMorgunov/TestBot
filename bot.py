
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Библиотека логирования.
import logging

# Файл настроек.
import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')
    
    # Передает входящее сообщение тому, кто на него подписался (после запуска команды в чате).
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greetUser))
    dp.add_handler(MessageHandler(Filters.text, talkToMe))

    # Ходить и проверять наличие новых сообщений.
    mybot.start_polling()

    # Бот будет работать до тех пор, пока мы его принудительно не остановим.
    mybot.idle()

def greetUser(bot, update):
    
    text = 'Вызван /start'
    logging.info(text)
    print(update)
    # Ответное сообщение пользователю.
    update.message.reply_text(text)

def talkToMe(bot, update):
    
    userText = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, ChatID: %s, Message: %s', update.message.chat.first_name, update.message.chat.id, update.message.text)
    # Ответное сообщение пользователю.
    update.message.reply_text(userText)

main()
