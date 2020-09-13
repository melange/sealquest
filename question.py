class Question:

    def __init__(self, text, hint, answer, success_message, fail_message):
        self.text = text
        self.hint = hint
        self.answer = answer
        self.success_message = success_message
        self.fail_message = fail_message


    def get_question(self):
        return self.text


    def get_hint(self):
        return self.hint


    def assess_answer(self, answer):
        if answer.lower() == self.answer.lower():
            return (True, self.success_message)
        else:
            return (False, self.fail_message)