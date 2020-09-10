import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class BotLogic:

    # Enable logging


    # Define a few command handlers. These usually take the two arguments update and
    # context. Error handlers also receive the raised TelegramError object in error.

    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def start(self, update, context):
        #Send a message when the command /start is issued
        update.message.reply_text('Hi!')

    def help(self, update, context):
        #Send a message when the command /help is issued
        update.message.reply_text('Help!')

    def echo(self, update, context):
        #Echo the user message
        update.message.reply_text(update.message.text)

    def error(self, update, context):
        #Log Errors caused by Updates
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)