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
    questions_provider = QuestionsProvider('questions.json')
    quest = Quest(questions_provider)
    bot = BotContainer(BotSettingsProvider(), BotLogic(quest))
    bot.start()

if __name__ == '__main__':
    main()