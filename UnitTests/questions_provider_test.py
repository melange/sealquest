from questions_provider import QuestionsProvider   # The code to test
import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch


class Test_QuestionsProvider(unittest.TestCase):
    def test_get_questions(self):
        questions_provider = QuestionsProvider(r'./UnitTests/test_questions.json')
        questions = questions_provider.get_questions()
        
        q1 = questions[0]
        q2 = questions[1]
        q3 = questions[2]

        self.assertEqual(len(questions), 3)
        
        self.assertEqual(q1.text, '2*2')
        self.assertEqual(q1.hint, '3+1')
        self.assertEqual(q1.answer, '4')
        self.assertEqual(q1.success_message, 'good work!')
        self.assertEqual(q1.fail_message, 'not quite right')

        self.assertEqual(q2.text, 'dog says')
        self.assertEqual(q2.hint, 'no hint for you')
        self.assertEqual(q2.answer, 'woof')
        self.assertEqual(q2.success_message, 'well done!')
        self.assertEqual(q2.fail_message, 'you can do better!')

        self.assertEqual(q3.text, 'The capital of the UK')
        self.assertEqual(q3.hint, 'Come on, you know it!')
        self.assertEqual(q3.answer, 'London')
        self.assertEqual(q3.success_message, 'nice!')
        self.assertEqual(q3.fail_message, 'try again')