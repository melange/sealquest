from bot_settings_provider import BotSettingsProvider   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch

@patch('bot_logic.BotLogic')
class Test_BotSettingsProvider(unittest.TestCase):

    @patch('os')
    def test_get_settings(self, os):
        
        settings_dict = dict()
        settings_dict['TelegramToken'] = '123:ABCDE'
        settings_dict['WebhookAppURL'] = 'https://some-app.herokuapp.com/'
        settings_dict['WebhookIP'] =  '0.0.0.0'
        settings_dict['PORT'] = 423
        settings_dict['QuestionsFile'] = 'questions.json'
        os.environ = settings_dict

        bot_settings_provider = BotSettingsProvider()
        settings = bot_settings_provider.get_settings()
        
        self.assertEqual(settings['token'], '123:ABCDE')
        self.assertEqual(settings['webhook_app_url'], 'https://some-app.herokuapp.com/')
        self.assertEqual(settings['webhook_ip'], '0.0.0.0')
        self.assertEqual(settings['webhook_port'], 423)
        self.assertEqual(settings['questions_file'], 'questions.json')

if __name__ == '__main__':
    unittest.main()
