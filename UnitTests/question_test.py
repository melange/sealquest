import unittest   # The test framework
from unittest.mock import MagicMock
from unittest.mock import patch
from question import Question

class Test_Question(unittest.TestCase):

    def test_init(self):
        text = 'my text'
        hint = 'my hint'
        answer = 'my answer'
        success_message = 'my success message'
        fail_message = 'my fail message'
        q = Question(text, hint, answer, success_message, fail_message)
        self.assertEqual(q.text, text)
        self.assertEqual(q.hint, hint)
        self.assertEqual(q.answer, answer)
        self.assertEqual(q.success_message, success_message)
        self.assertEqual(q.fail_message, fail_message)


    def test_assess_answer_true(self):
        text = 'my text'
        hint = 'my hint'
        answer = 'my answer'
        success_message = 'my success message'
        fail_message = 'my fail message'
        q = Question(text, hint, answer, success_message, fail_message)
        user_answer = 'mY aNsweR'
        (result, message) = q.assess_answer(user_answer)
        self.assertEqual(result, True)
        self.assertEqual(message, q.success_message)

    def test_assess_answer_false(self):
        text = 'my text'
        hint = 'my hint'
        answer = 'my answer'
        success_message = 'my success message'
        fail_message = 'my fail message'
        q = Question(text, hint, answer, success_message, fail_message)
        user_answer = 'wrong answer'
        (result, message) = q.assess_answer(user_answer)
        self.assertEqual(result, False)
        self.assertEqual(message, q.fail_message)