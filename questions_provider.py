from question import Question
import logging
import json

class QuestionsProvider:

    def __init__(self, questions_file):
        self.questions_file = questions_file
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_questions(self):
        
        try:
            with open(self.questions_file) as json_file:
                data = json.load(json_file)
                questions = list()
                for q in data['questions']:
                    text = q['text']
                    hint = q['hint']
                    answer = q['answer']
                    success_message = q['success_message']
                    fail_message = q['fail_message']
                    question = Question(text, hint, answer, success_message, fail_message)
                    questions.append(question)
        except IOError:
            self.logger.error("No questions in the provided file")
            questions = []

        return questions