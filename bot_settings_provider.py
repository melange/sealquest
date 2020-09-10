import os 

class BotSettingsProvider:
    
    def get_settings(self):
        settings = dict()
        settings['token'] = os.environ['TelegramToken']
        settings['webhook_app_url'] = os.environ['WebhookAppURL']
        settings['webhook_ip'] = os.environ['WebhookIP']
        settings['webhook_port'] = os.environ['WebhookPort']
        return settings