import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class BotLogic:

    def __init__(self):
        self.is_started = False
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def start(self, update, context):
        if self.is_started == False:
            update.message.reply_text('Hi!')
            self.is_started = True
        else:
            update.message.reply_text('Already started')


    def help(self, update, context):
        update.message.reply_text('Help')


    def echo(self, update, context):
        update.message.reply_text(update.message.text)


    def error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)