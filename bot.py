import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import json
from questions_provider import QuestionsProvider
from bot_container import BotContainer
from bot_logic import BotLogic
from quest import Quest
from bot_settings_provider import BotSettingsProvider


def main():
    settings_provider = BotSettingsProvider()
    questions_provider = QuestionsProvider(settings_provider)
    quest = Quest(questions_provider)
    bot = BotContainer(settings_provider, BotLogic(quest))
    bot.start()

if __name__ == '__main__':
    main()