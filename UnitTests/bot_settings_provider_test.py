from bot_settings_provider import BotSettingsProvider   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch

@patch('bot_logic.BotLogic')
class Test_BotSettingsProvider(unittest.TestCase):

    @patch('os')
    def test_get_settings(self, os):
        
        settings_dict = dict()
        settings_dict['TelegramToken'] = '1389512183:AAHIV1J5B67VpIbsxQyxgoZJ_Qion3kcpvg'
        settings_dict['WebhookAppURL'] = 'https://seal-quest-bot.herokuapp.com/'
        settings_dict['WebhookIP'] =  '0.0.0.0'
        settings_dict['WebhookPort'] = 5000
        os.environ = settings_dict

        bot_settings_provider = BotSettingsProvider()
        settings = bot_settings_provider.get_settings()
        
        self.assertEqual(settings['token'], '1389512183:AAHIV1J5B67VpIbsxQyxgoZJ_Qion3kcpvg')
        self.assertEqual(settings['webhook_app_url'], 'https://seal-quest-bot.herokuapp.com/')
        self.assertEqual(settings['webhook_ip'], '0.0.0.0')
        self.assertEqual(settings['webhook_port'], 5000)


if __name__ == '__main__':
    unittest.main()
