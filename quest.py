class Quest:

    def __init__(self, questions_provider):
        self.messages = dict()
        self.messages['quest_already_started'] = 'Quest is already running'
        self.messages['quest_not_started'] = 'Use /start to start the quest'
        self.messages['quest_ended'] = 'Quest is ended. Use /start to start the quest'
        self.messages['welcome'] = 'Welcome to the seal quest!'
        self.messages['finish'] = 'Congratulations! You have passed the seal quest!'
        self.messages['correct_answer'] = 'Nice! Keep going!'
        self.messages['incorrect_answer'] = 'Try again!'
        self.questions = questions_provider.get_questions()


    def process_message(self, message):
        pass


    def start_quest(self):
        self.current_question_number = 0
        self.current_question = self.questions[self.current_question_number]
        return self.current_question.get_question()


    def get_current_question(self):
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


    def end_quest(self):
        pass