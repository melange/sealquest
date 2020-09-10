from bot_container import BotContainer   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch

@patch('bot_logic.BotLogic')
class Test_BotContainer(unittest.TestCase):

    def test_read_settings(self, logic):
        import bot_logic
        botContainer = BotContainer('settings.json', logic)
        self.assertEqual(botContainer.token, '1389512183:AAHIV1J5B67VpIbsxQyxgoZJ_Qion3kcpvg')


if __name__ == '__main__':
    unittest.main()
