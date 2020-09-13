from question import Question
import json

class QuestionsProvider:

    def __init__(self, questions_file):
        self.questions_file = questions_file

    def get_questions(self):
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

        return questions