from questions_provider import QuestionsProvider  
from quest import Quest
import unittest  
from unittest.mock import MagicMock
from unittest.mock import patch


class Test_Quest(unittest.TestCase):

    @patch('questions_provider.QuestionsProvider')
    def test_start_quest(self, questions_provider):
        
        q1 = MagicMock()
        q1.text = '2*2'
        q1.hint = '3+1'
        q1.answer = '4'
        q1.success_message = 'good work!'
        q1.fail_message = 'not quite right'

        q2 = MagicMock()
        q2.text = 'dog says'
        q2.hint = 'no hint for you'
        q2.answer = 'woof'
        q2.success_message = 'well done!'
        q2.fail_message = 'you can do better!'

        q3 = MagicMock()
        q3.text = '2*2'
        q3.hint = '3+1'
        q3.answer = '4'
        q3.success_message = 'good work!'
        q3.fail_message = 'not quite right'

        questions_provider.get_questions.return_value = [q1, q2, q3]

        quest = Quest(questions_provider)

        message = quest.start_quest()
        self.assertEqual(quest.current_question, q1)
        self.assertEqual(message, q1.get_question)
