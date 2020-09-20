import logging
from quest_message import QuestMessage

class Quest:

    messages = dict()
    messages['quest_already_started'] = 'Quest is already running'
    messages['quest_not_started'] = 'Quest is not started'
    messages['quest_ended'] = 'Quest is ended.'
    messages['welcome'] = 'Welcome to the seal quest!'
    messages['finish'] = 'Congratulations! You have passed the seal quest!'
    messages['correct_answer'] = 'Nice! Keep going!'
    messages['incorrect_answer'] = 'Try again!'

    def __init__(self, questions_provider):
        if questions_provider is None:
            logging.error("questions_provider is none")
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
            messages_list.append(QuestMessage(self.messages['welcome'], False))
            messages_list += self.get_question_text()
        else:
            messages_list.append(QuestMessage(self.messages['quest_already_started'],False))
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
            messages_list.append(QuestMessage("Question {0:d} of {1:d}".format(self.current_question_number + 1, len(self.questions)),False))
            messages_list.append(QuestMessage(self.get_current_question().get_question(), False))
            self.logger.info("Question displayed: %d" % (self.current_question_number + 1))
        else:
            messages_list.append(QuestMessage(self.messages['quest_not_started'], False))
        return messages_list


    def get_hint(self):
        messages_list = list()
        if self.is_started:
            messages_list.append(QuestMessage(self.get_current_question().get_hint(), False))
            self.logger.info("Hint displayed: %d" % (self.current_question_number + 1))
        else:
            messages_list.append(QuestMessage(self.messages['quest_not_started'], False))
        return messages_list


    def assess_answer(self, answer):
        messages_list = list()
        if self.is_started:
            (result, message) = self.get_current_question().assess_answer(answer)
            messages_list.append(QuestMessage(message, True))
            if result == True:
                messages_list.append(QuestMessage(self.messages['correct_answer'], True))
                question = self.next_question()
                if question is not None:
                    messages_list += self.get_question_text()
                else:
                    messages_list.append(QuestMessage(self.messages['finish'], False))
                    self.is_started = False
            else:
                messages_list.append(QuestMessage(self.messages['incorrect_answer'], True))
            self.logger.info("Answer for question %d assesed. Given Answer: %s. Result: %s", (self.current_question_number + 1), answer, result)
        else:
            messages_list.append(QuestMessage(self.messages['quest_not_started'], True))
        return messages_list


    def end_quest(self):
        messages_list = list()
        if self.is_started:
            self.is_started = False
            self.logger.info("Quest ended")
            messages_list.append(QuestMessage(self.messages['quest_ended'], False))
        else:
            messages_list.append(QuestMessage(self.messages['quest_not_started'], False))
        return messages_list    