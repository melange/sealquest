from bot_settings_provider import BotSettingsProvider
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch


class Test_BotSettingsProvider(unittest.TestCase):

    #@patch('os.environment')
    @patch.dict('os.environ', 
        {
            'TelegramToken': '123:ABCDE',
            'WebhookAppURL': 'https://some-app.herokuapp.com/',
            'WebhookIP': '0.0.0.0',
            'PORT': '423',
            'QuestionsFile': 'questions.json'
        }
    )
    def test_get_settings(self):
        
        #settings_dict = dict()
        #settings_dict['TelegramToken'] = '123:ABCDE'
        #settings_dict['WebhookAppURL'] = 'https://some-app.herokuapp.com/'
        #settings_dict['WebhookIP'] =  '0.0.0.0'
        #settings_dict['PORT'] = 423
        #settings_dict['QuestionsFile'] = 'questions.json'
        #mocked_environ = settings_dict

        bot_settings_provider = BotSettingsProvider()
        settings = bot_settings_provider.get_settings()
        
        self.assertEqual(settings['token'], '123:ABCDE')
        self.assertEqual(settings['webhook_app_url'], 'https://some-app.herokuapp.com/')
        self.assertEqual(settings['webhook_ip'], '0.0.0.0')
        self.assertEqual(int(settings['webhook_port']), 423)
        self.assertEqual(settings['questions_file'], 'questions.json')


if __name__ == '__main__':
    unittest.main()
