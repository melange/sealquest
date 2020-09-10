import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import json
from bot_container import BotContainer
from bot_logic import BotLogic


def main():
    bot = BotContainer('settings.json', BotLogic())
    bot.start()

if __name__ == '__main__':
    main()