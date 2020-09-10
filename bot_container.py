from bot_logic import BotLogic
import json
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class BotContainer:

    def __init__(self, settings_filename, bot_logic):
        self.logic = bot_logic

        self.read_settings(settings_filename)

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self._updater = Updater(self.token, use_context=True)
        self._dp = self._updater.dispatcher
        self.register_handlers()


    def read_settings(self, settings_filename):
        with open(settings_filename, 'r') as json_file:
            settings_json = json.load(json_file)
        self.token = settings_json['TelegramToken']
        self.webhook_app_url = settings_json['WebhookAppURL']
        self.webhook_ip = settings_json['WebhookIP']
        self.webhook_port = settings_json['WebhookPort']


    def register_handlers(self):
        self._dp.add_handler(CommandHandler("start", self.logic.start))
        self._dp.add_handler(CommandHandler("help", self.logic.help))
        self._dp.add_handler(MessageHandler(Filters.text, self.logic.echo))
        self._dp.add_error_handler(self.logic.error)


    def start(self):
        self._updater.start_webhook(self.webhook_ip,
                          port = int(self.webhook_port),
                          url_path = self.token)
        self._updater.bot.setWebhook(self.webhook_app_url + self.token)
        self._updater.idle()