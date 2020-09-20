from bot_logic import BotLogic   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch

class Test_BotLogic(unittest.TestCase):

    def test_init_with_valid_quest(self):
        quest = MagicMock()
        bot_logic = BotLogic(quest)


    def test_init_with_none_quest(self):
        quest = None
        with self.assertRaises(AttributeError):
            bot_logic = BotLogic(quest)


    def test_start_if_running(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.start(update, context)
        self.assertEqual(bot_logic.is_started, True)
        self.fail()


    def test_start_if_not_running(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        bot_logic.start(update, context)
        self.assertEqual(bot_logic.is_started, True)
        self.fail()


    def test_stop_if_running(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.stop(update, context)
        self.assertEqual(bot_logic.is_started, False)
        self.fail()


    def test_stop_if_not_running(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        bot_logic.stop(update, context)
        self.assertEqual(bot_logic.is_started, False)
        self.fail()

    
    def test_send_messages_none_context(self):
        self.fail()


    def test_send_messages_none_updater(self):
        self.fail()


    def test_send_messages_none_messages_list(self):
        self.fail()


    def test_send_messages_empty_messages_list(self):
        self.fail()

    
    def test_send_messages_filled_messages_list(self):
        self.fail()


    def test_help_if_running(self):
        self.fail()


    def test_help_if_not_running(self):
        self.fail()


    def test_hint_if_running(self):
        self.fail()


    def test_hint_if_not_running(self):
        self.fail()


    def test_answer_if_running(self):
        self.fail()


    def test_answer_if_not_running(self):
        self.fail()


    def test_error(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
