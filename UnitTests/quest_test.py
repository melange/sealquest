from questions_provider import QuestionsProvider  
from quest import Quest
import unittest  
from unittest.mock import MagicMock
from unittest.mock import patch


class Test_Quest(unittest.TestCase):

    def generate_questions_list(self):
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

        questions_list = [q1, q2, q3]
        return questions_list

    def test_init_with_null_questions_provider(self):
        with self.assertRaises(AttributeError):
            quest = Quest(None)


    @patch('questions_provider.QuestionsProvider')
    def test_init_with_valid_questions_provider(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        self.assertEquals(quest.questions, questions_provider.get_questions())


    @patch('questions_provider.QuestionsProvider')
    def test_init_with_empty_questions_provider(self, questions_provider):
        questions_provider.get_questions.return_value = list()
        with self.assertRaises(AttributeError):
            quest = Quest(None)


    @patch('questions_provider.QuestionsProvider')
    def test_init_with_none_questions_list_in_questions_provider(self, questions_provider):
        questions_provider.get_questions.return_value = None
        with self.assertRaises(AttributeError):
            quest = Quest(None)


    @patch('questions_provider.QuestionsProvider')
    def test_start_quest_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        messages_list = quest.start_quest()
        self.assertEqual(quest.is_started, True)
        self.assertEqual(len(messages_list), 3)
        self.assertEqual(quest.get_current_question(), questions_provider.get_questions()[0])
        self.assertEqual(quest.current_question_number, 0)
        self.assertEqual(messages_list[0].text, quest.messages['welcome'])
        self.assertEqual(messages_list[0].as_reply, False)
        self.assertEqual(messages_list[1].text, 'Question 1 of 3')
        self.assertEqual(messages_list[1].as_reply, False)
        self.assertEqual(messages_list[2].text, questions_provider.get_questions()[0].get_question())
        self.assertEqual(messages_list[2].as_reply, False)

    @patch('questions_provider.QuestionsProvider')
    def test_start_quest_if_already_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 2
        messages_list = quest.start_quest()
        self.assertEqual(quest.is_started, True)
        self.assertEqual(quest.get_current_question(), questions_provider.get_questions()[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_already_started'])
        self.assertEqual(messages_list[0].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_get_current_question_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        q3 = questions_list[2]
        q3.get_question.return_value = q3.text
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 2
        messages_list = quest.get_question_text()
        self.assertEqual(quest.get_current_question(), questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 2)
        self.assertEqual(messages_list[0].text, 'Question 3 of 3')
        self.assertEqual(messages_list[0].as_reply, False)
        self.assertEqual(messages_list[1].text, questions_list[2].get_question())
        self.assertEqual(messages_list[1].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_get_current_question_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question_number = 2
        messages_list = quest.get_question_text()
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_not_started'])
        self.assertEqual(messages_list[0].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_get_hint_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 2
        messages_list = quest.get_hint()
        self.assertEqual(quest.get_current_question(), questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, questions_list[2].get_hint())
        self.assertEqual(messages_list[0].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_get_hint_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question_number = 2
        messages_list = quest.get_hint()
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_not_started'])
        self.assertEqual(messages_list[0].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_started_correct_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        q2 = questions_list[1]
        q2.assess_answer.return_value = (True, q2.success_message)
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 1
        
        messages_list = quest.assess_answer(questions_list[1].answer)
        
        self.assertEqual(quest.get_current_question(), questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 4)
        self.assertEqual(messages_list[0].text, questions_list[1].success_message)
        self.assertEqual(messages_list[0].as_reply, True)
        self.assertEqual(messages_list[1].text, quest.messages['correct_answer'])
        self.assertEqual(messages_list[1].as_reply, True)
        self.assertEqual(messages_list[2].text, 'Question 3 of 3')
        self.assertEqual(messages_list[2].as_reply, False)
        self.assertEqual(messages_list[3].text, questions_list[2].get_question())
        self.assertEqual(messages_list[3].as_reply, False)

    
    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_not_started_correct_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        q2 = questions_list[1]
        q2.assess_answer.return_value = (True, q2.success_message)
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question_number = 1
        
        messages_list = quest.assess_answer(questions_list[1].answer)
        
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_not_started'])
        self.assertEqual(messages_list[0].as_reply, True)


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_started_incorrect_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        q2 = questions_list[1]
        q2.assess_answer.return_value = (False, q2.fail_message)
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 1
        
        messages_list = quest.assess_answer(questions_list[1].answer  + 'abc')
        
        self.assertEqual(quest.get_current_question(), questions_list[1])
        self.assertEqual(quest.current_question_number, 1)
        self.assertEqual(len(messages_list), 2)
        self.assertEqual(messages_list[0].text, questions_list[1].fail_message)
        self.assertEqual(messages_list[0].as_reply, True)
        self.assertEqual(messages_list[1].text, quest.messages['incorrect_answer'])
        self.assertEqual(messages_list[1].as_reply, True)


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_not_started_incorrect_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        q2 = questions_list[1]
        q2.assess_answer.return_value = (False, q2.fail_message)
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question_number = 1
        
        messages_list = quest.assess_answer(questions_list[1].answer + 'abc')
        
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_not_started'])
        self.assertEqual(messages_list[0].as_reply, True)


    @patch('questions_provider.QuestionsProvider')    
    def test_assess_answer_if_started_correct_answer_last_question(self, questions_provider):
        questions_list = self.generate_questions_list()
        q3 = questions_list[2]
        q3.assess_answer.return_value = (True, q3.success_message)
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 2
        
        messages_list = quest.assess_answer(questions_list[2].answer)
        
        self.assertEqual(len(messages_list), 3)
        self.assertEqual(messages_list[0].text, questions_list[2].success_message)
        self.assertEqual(messages_list[0].as_reply, True)
        self.assertEqual(messages_list[1].text, quest.messages['correct_answer'])
        self.assertEqual(messages_list[1].as_reply, True)
        self.assertEqual(messages_list[2].text, quest.messages['finish'])
        self.assertEqual(messages_list[2].as_reply, False)
        self.assertEqual(quest.is_started, False)


    @patch('questions_provider.QuestionsProvider')
    def test_end_quest_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question_number = 2
        messages_list = quest.end_quest()
        self.assertEqual(quest.is_started, False)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_ended'])
        self.assertEqual(messages_list[0].as_reply, False)


    @patch('questions_provider.QuestionsProvider')
    def test_end_quest_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question_number = 2
        messages_list = quest.end_quest()
        self.assertEqual(quest.is_started, False)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].text, quest.messages['quest_not_started'])
        self.assertEqual(messages_list[0].as_reply, False)


if __name__ == '__main__':
    unittest.main()