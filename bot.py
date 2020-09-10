import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import json
from bot_container import BotContainer
from bot_logic import BotLogic
from bot_settings_provider import BotSettingsProvider


def main():
    bot = BotContainer(BotSettingsProvider(), BotLogic())
    bot.start()

if __name__ == '__main__':
    main()