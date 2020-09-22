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


    def test_handle_message_start(self):
        quest = MagicMock()
        update = MagicMock()
        update.message.text = '/start'
        context = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.start = MagicMock(return_value = [])
        bot_logic.handle_message(update, context)
        
        bot_logic.start.assert_called_once()


    def test_handle_message_stop(self):
        quest = MagicMock()
        update = MagicMock()
        update.message.text = '/stop'
        context = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.stop = MagicMock(return_value = [])
        bot_logic.handle_message(update, context)
        
        bot_logic.stop.assert_called_once()


    def test_handle_message_hint(self):
        quest = MagicMock()
        update = MagicMock()
        update.message.text = '/hint'
        context = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.hint = MagicMock(return_value = [])
        bot_logic.handle_message(update, context)
        
        bot_logic.hint.assert_called_once()


    def test_handle_message_help(self):
        quest = MagicMock()
        update = MagicMock()
        update.message.text = '/help'
        context = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.help = MagicMock(return_value = [])
        bot_logic.handle_message(update, context)
        
        bot_logic.help.assert_called_once()


    def test_handle_message_answer(self):
        quest = MagicMock()
        update = MagicMock()
        update.message.text = 'abc'
        context = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.answer = MagicMock(return_value = [])
        bot_logic.handle_message(update, context)
        
        bot_logic.answer.assert_called_once()


    def test_send_messages_none_context(self):
        quest = MagicMock()
        update = MagicMock()
        context = None
        messages_list = MagicMock()

        bot_logic = BotLogic(quest)
        
        with self.assertRaises(AttributeError):
            bot_logic.send_messages(update, context, messages_list)


    def test_send_messages_none_update(self):
        quest = MagicMock()
        update = None
        context = MagicMock()
        messages_list = MagicMock()

        bot_logic = BotLogic(quest)
        
        with self.assertRaises(AttributeError):
            bot_logic.send_messages(update, context, messages_list)


    def test_send_messages_none_messages_list(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        messages_list = None

        bot_logic = BotLogic(quest)
        
        with self.assertRaises(AttributeError):
            bot_logic.send_messages(update, context, messages_list)


    def test_send_messages_empty_messages_list(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        context.bot.send_message.return_value = None
        messages_list = []

        bot_logic = BotLogic(quest)
        bot_logic.send_messages(update, context, messages_list)

        context.bot.send_message.assert_not_called()

    
    def test_send_messages_filled_messages_list(self):
        quest = MagicMock()
        update = MagicMock()
        context = MagicMock()
        context.bot.send_message.return_value = None
        
        msg1 = MagicMock()
        msg1.text = 'abc'
        msg1.as_repy = False
        msg2 = MagicMock()
        msg2.text = 'def'
        msg2.as_repy = True
        messages_list = [msg1, msg2]

        bot_logic = BotLogic(quest)
        bot_logic.send_messages(update, context, messages_list)

        self.assertEqual(context.bot.send_message.call_count, 2)


    def test_start_if_running(self):
        quest = MagicMock()
        quest.start_quest.return_value = []

        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.start(

        )
        self.assertEqual(bot_logic.is_started, True)
        quest.start_quest.assert_not_called()


    def test_start_if_not_running(self):
        quest = MagicMock()
        quest.start_quest.return_value = []
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        bot_logic.start()
        
        self.assertEqual(bot_logic.is_started, True)
        quest.start_quest.assert_called_once()


    def test_stop_if_running(self):
        quest = MagicMock()
        quest.end_quest.return_value = []
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.stop()
        
        self.assertEqual(bot_logic.is_started, False)
        quest.end_quest.assert_called_once()


    def test_stop_if_not_running(self):
        quest = MagicMock()
        quest.end_quest.return_value = []
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        messages_list = bot_logic.stop()
        
        self.assertEqual(bot_logic.is_started, False)
        quest.end_quest.assert_not_called()
        self.assertEqual(messages_list[0].text, bot_logic.messages['bot_not_started'])
        self.assertEqual(len(messages_list), 1)


    def test_help_if_running(self):
        quest = MagicMock()
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        messages_list = bot_logic.help()
        
        self.assertEqual(bot_logic.is_started, True)
        self.assertEqual(messages_list[0].text, bot_logic.messages['help'])
        self.assertEqual(len(messages_list), 1)


    def test_help_if_not_running(self):
        quest = MagicMock()

        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        messages_list = bot_logic.help()
        
        self.assertEqual(bot_logic.is_started, False)
        self.assertEqual(messages_list[0].text, bot_logic.messages['help'])
        self.assertEqual(len(messages_list), 1)


    def test_hint_if_running(self):
        quest = MagicMock()
        quest.get_hint.return_value = []
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.hint()
        
        self.assertEqual(bot_logic.is_started, True)
        quest.get_hint.assert_called_once()


    def test_hint_if_not_running(self):
        quest = MagicMock()
        quest.get_hint.return_value = []
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        messages_list = bot_logic.hint()
        
        self.assertEqual(bot_logic.is_started, False)
        quest.get_hint.assert_not_called()
        self.assertEqual(messages_list[0].text, bot_logic.messages['bot_not_started'])
        self.assertEqual(len(messages_list), 1)


    def test_answer_if_running(self):
        quest = MagicMock()
        quest.assess_answer.return_value = []
        answer_text = 'abc'
        
        bot_logic = BotLogic(quest)
        bot_logic.is_started = True
        bot_logic.answer(answer_text)
        
        self.assertEqual(bot_logic.is_started, True)
        quest.assess_answer.assert_called_once()


    def test_answer_if_not_running(self):
        quest = MagicMock()
        quest.assess_answer.return_value = []
        answer_text = 'abc'

        bot_logic = BotLogic(quest)
        bot_logic.is_started = False
        messages_list = bot_logic.answer(answer_text)
        
        self.assertEqual(bot_logic.is_started, False)
        quest.assess_answer.assert_not_called()
        self.assertEqual(messages_list[0].text, bot_logic.messages['bot_not_started'])
        self.assertEqual(len(messages_list), 1)


if __name__ == '__main__':
    unittest.main()
