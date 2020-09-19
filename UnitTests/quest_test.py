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


    @patch('questions_provider.QuestionsProvider')
    def test_start_quest_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        messages_list = quest.start_quest()
        self.assertEqual(quest.is_started, True)
        self.assertEqual(len(messages_list), 2)
        self.assertEqual(quest.current_question, questions_provider.get_questions()[0])
        self.assertEqual(quest.current_question_number, 0)
        self.assertEqual(messages_list[0], quest.messages['welcome'])
        self.assertEqual(messages_list[1], questions_provider.get_questions()[0].get_question())

    @patch('questions_provider.QuestionsProvider')
    def test_start_quest_if_already_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[2]
        quest.current_question_number = 2
        messages_list = quest.start_quest()
        self.assertEqual(quest.is_started, True)
        self.assertEqual(quest.current_question, questions_provider.get_questions()[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_already_started'])

    @patch('questions_provider.QuestionsProvider')
    def test_get_current_question_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[2]
        messages_list = quest.get_current_question()
        self.assertEqual(quest.current_question, questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], questions_list[2].get_question)


    @patch('questions_provider.QuestionsProvider')
    def test_get_current_question_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question = questions_list[2]
        messages_list = quest.get_current_question()
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_not_started'])


    @patch('questions_provider.QuestionsProvider')
    def test_get_hint_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[2]
        messages_list = quest.get_hint()
        self.assertEqual(quest.current_question, questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], questions_list[2].get_hint())


    @patch('questions_provider.QuestionsProvider')
    def test_get_hint_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question = questions_list[2]
        messages_list = quest.get_hint()
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_not_started'])


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_started_correct_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[1]
        
        messages_list = quest.assess_answer(questions_list[1].answer)
        
        self.assertEqual(quest.current_question, questions_list[2])
        self.assertEqual(quest.current_question_number, 2)
        self.assertEqual(len(messages_list), 3)
        self.assertEqual(messages_list[0], questions_list[1].success_message)
        self.assertEqual(messages_list[1], quest.messages['correct_answer'])
        self.assertEqual(messages_list[2], questions_list[2].get_question)

    
    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_not_started_correct_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[1]
        
        messages_list = quest.assess_answer(questions_list[1].answer)
        
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_not_started'])


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_started_incorrect_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[1]
        
        messages_list = quest.assess_answer(questions_list[1].answer  + 'abc')
        
        self.assertEqual(quest.current_question, questions_list[1])
        self.assertEqual(quest.current_question_number, 1)
        self.assertEqual(len(messages_list), 2)
        self.assertEqual(messages_list[0], questions_list[1].fail_message)
        self.assertEqual(messages_list[1], quest.messages['incorrect_answer'])


    @patch('questions_provider.QuestionsProvider')
    def test_assess_answer_if_not_started_incorrect_answer(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[1]
        
        messages_list = quest.assess_answer(questions_list[1].answer + 'abc')
        
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_not_started'])


    @patch('questions_provider.QuestionsProvider')    
    def test_assess_answer_if_not_started_correct_answer_last_question(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = True
        quest.current_question = questions_list[2]
        
        messages_list = quest.assess_answer(questions_list[2].answer)
        
        self.assertEqual(len(messages_list), 3)
        self.assertEqual(messages_list[0], questions_list[1].success_message)
        self.assertEqual(messages_list[1], quest.messages['correct_answer'])
        self.assertEqual(messages_list[2], quest.messages['finish'])
        self.assertEqual(quest.is_started, False)


    @patch('questions_provider.QuestionsProvider')
    def test_end_quest_if_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question = questions_list[2]
        messages_list = quest.end_quest()
        self.assertEqual(quest.is_started, False)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_ended'])


    @patch('questions_provider.QuestionsProvider')
    def test_end_quest_if_not_started(self, questions_provider):
        questions_list = self.generate_questions_list()
        questions_provider.get_questions.return_value = questions_list
        quest = Quest(questions_provider)
        quest.is_started = False
        quest.current_question = questions_list[2]
        messages_list = quest.end_quest()
        self.assertEqual(quest.is_started, False)
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0], quest.messages['quest_not_started'])


if __name__ == '__main__':
    unittest.main()