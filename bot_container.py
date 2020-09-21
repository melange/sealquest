from bot_logic import BotLogic
from bot_settings_provider import BotSettingsProvider
import json
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class BotContainer:

    def __init__(self, bot_settings_provider, bot_logic):
        self.logic = bot_logic

        self.get_settings(bot_settings_provider)

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self._updater = Updater(self.token, use_context=True)
        self._dp = self._updater.dispatcher
        self.register_handlers()


    def get_settings(self, bot_settings_provider):
        settings = bot_settings_provider.get_settings()
        self.token = settings['token']
        self.webhook_app_url = settings['webhook_app_url']
        self.webhook_ip = settings['webhook_ip']
        self.webhook_port = settings['webhook_port']



    def register_handlers(self):
        #self._dp.add_handler(CommandHandler("start", self.logic.start))
        #self._dp.add_handler(CommandHandler("stop", self.logic.stop))
        #self._dp.add_handler(CommandHandler("help", self.logic.help))
        #self._dp.add_handler(CommandHandler("hint", self.logic.hint))
        self._dp.add_handler(MessageHandler(Filters.text | Filters.command, self.logic.handle_message))
        self._dp.add_error_handler(self.logic.error)


    def start(self):
        self._updater.start_webhook(self.webhook_ip,
                          port = int(self.webhook_port),
                          url_path = self.token)
        self._updater.bot.setWebhook(self.webhook_app_url + self.token)
        self._updater.idle()