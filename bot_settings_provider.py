import os 

class BotSettingsProvider:
    
    def __init__(self):
        self.settings = self.get_settings()
    
    def get_settings(self):
        settings = dict()
        settings['token'] = os.environ['TelegramToken']
        settings['webhook_app_url'] = os.environ['WebhookAppURL']
        settings['webhook_ip'] = os.environ['WebhookIP']
        settings['webhook_port'] = int(os.environ.get('PORT', 5000))
        settings['questions_file'] = os.environ['QuestionsFile']
        settings['database_url'] = os.environ['DATABASE_URL']
        return settings