from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(
    format='%(asctime)s-%(levelname)s-%(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(bot,update):
    text="вызван start"
    print(text)
    update.message.reply_text(text)

def took_ty_me(bot,update):
    user_text=update.message.text
   
    
    print(update.message)
    update.message.reply_text(user_text)

def main():
    myBot=Updater(settings.API_KEY,request_kwargs=settings.PROXY)
    logging.info('start bot')
    dp=myBot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(MessageHandler(Filters.text,took_ty_me))
    myBot.start_polling()
    myBot.idle()

main()
