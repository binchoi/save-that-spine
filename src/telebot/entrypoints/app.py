
import logging
import os
import random
import string

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
        Welcome to _Save That Spine_ <br /> To create a new race, send _create_. 
        To join an existing race, send _join <race-code>_ (include the actual 
        race code you have received from your fellow racer)
        """,
        parse_mode="markdown",
    )


def start_race(update: Update, context: CallbackContext):
    user = update.effective_user

    # generate random race_code
    letters = string.ascii_lowercase
    race_code = ''.join(random.choice(letters) for i in range(6))



# def echo(update: Update, context: CallbackContext):
#     message = f"You say, _{update.message.text}_, I say *cool, idc*"
#     context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=message,
#         parse_mode="markdown",
#     )


if __name__ == '__main__':
    # create the updater
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # get dispatcher to register handlers
    dispatcher = updater.dispatcher

    # register handlers
    dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # start the bot
    updater.start_polling()

    updater.idle()

