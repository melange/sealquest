from bot_container import BotContainer   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch


class Test_BotContainer(unittest.TestCase):

    @patch('bot_settings_provider.BotSettingsProvider')
    @patch('bot_logic.BotLogic')
    def test_read_settings(self, settings_provider, logic):
        import bot_settings_provider
        import bot_logic

        settings_dict = dict()
        settings_dict['token'] = '1389512183:AAHIV1J5B67VpIbsxQyxgoZJ_Qion3kcpvg'
        settings_dict['webhook_app_url'] = 'https://seal-quest-bot.herokuapp.com/'
        settings_dict['webhook_ip'] =  '0.0.0.0'
        settings_dict['webhook_port'] = 5000
        settings_provider.settings = settings_dict

        botContainer = BotContainer(settings_provider, logic)
        self.assertEqual(botContainer.token, '1389512183:AAHIV1J5B67VpIbsxQyxgoZJ_Qion3kcpvg')
        self.assertEqual(botContainer.webhook_app_url, 'https://seal-quest-bot.herokuapp.com/')
        self.assertEqual(botContainer.webhook_ip, '0.0.0.0')
        self.assertEqual(botContainer.webhook_port, 5000)


if __name__ == '__main__':
    unittest.main()
