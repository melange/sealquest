class Quest:

    def __init__(self, questions_provider):
        self.questions = questions_provider.get_questions()


    def start_quest(self):
        self.current_question_number = 0
        self.current_question = self.questions[self.current_question_number]
        return self.current_question.get_question()


    def get_hint(self):
        return self.current_question.get_hint()


    def assess_answer(self, answer):
        (result, message) = self.current_question.assess_answer(answer)
        output_message = message
        if result == True:
            self.current_question_number += 1 
            if self.current_question_number < len(self.questions):
                self.current_question = self.questions[self.current_question_number]
                output_message += '\n' + self.current_question.get_question()
            else:
                output_message += '\n' + 'Quest completed!'
        return output_message