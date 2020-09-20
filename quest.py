import logging

class Quest:

    def __init__(self, questions_provider):
        if questions_provider is None:
            logging.error("questions_provider is none")
        self.messages = dict()
        self.messages['quest_already_started'] = 'Quest is already running'
        self.messages['quest_not_started'] = 'Use /start to start the quest'
        self.messages['quest_ended'] = 'Quest is ended. Use /start to start the quest'
        self.messages['welcome'] = 'Welcome to the seal quest!'
        self.messages['finish'] = 'Congratulations! You have passed the seal quest!'
        self.messages['correct_answer'] = 'Nice! Keep going!'
        self.messages['incorrect_answer'] = 'Try again!'
        self.questions = questions_provider.get_questions()
        self.current_question_number = 0
        self.is_started = False
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def start_quest(self):
        messages_list = list()
        if not self.is_started:
            self.current_question_number = 0
            self.is_started = True
            self.logger.info("Quest started")
            messages_list.append(self.messages['welcome'])
            messages_list += self.get_question_text()
        else:
            messages_list.append(self.messages['quest_already_started'])
        return messages_list    

    def get_current_question(self):
        return self.questions[self.current_question_number]

    def next_question(self):
        if self.current_question_number +  1 < len(self.questions):
            self.current_question_number += 1
            return self.get_current_question()
        else:
            return None

    def get_question_text(self):
        messages_list = list()
        if self.is_started:
            messages_list.append("Question {0:d} of {1:d}".format(self.current_question_number + 1, len(self.questions)))
            messages_list.append(self.get_current_question().get_question())
            self.logger.info("Question displayed: %d" % (self.current_question_number + 1))
        else:
            messages_list.append(self.messages['quest_not_started'])
        return messages_list


    def get_hint(self):
        messages_list = list()
        if self.is_started:
            messages_list.append(self.get_current_question().get_hint())
            self.logger.info("Hint displayed: %d" % (self.current_question_number + 1))
        else:
            messages_list.append(self.messages['quest_not_started'])
        return messages_list


    def assess_answer(self, answer):
        messages_list = list()
        if self.is_started:
            (result, message) = self.get_current_question().assess_answer(answer)
            messages_list.append(message)
            if result == True:
                messages_list.append(self.messages['correct_answer'])
                question = self.next_question()
                if question is not None:
                    messages_list += self.get_question_text()
                else:
                    messages_list.append(self.messages['finish'])
                    self.is_started = False
            else:
                messages_list.append(self.messages['incorrect_answer'])
            self.logger.info("Answer for question %d assesed. Given Answer: %s. Result: %s", (self.current_question_number + 1), answer, result)
        else:
            messages_list.append(self.messages['quest_not_started'])
        return messages_list


    def end_quest(self):
        messages_list = list()
        if self.is_started:
            self.is_started = False
            self.logger.info("Quest ended")
            messages_list.append(self.messages['quest_ended'])
        else:
            messages_list.append(self.messages['quest_not_started'])
        return messages_list    