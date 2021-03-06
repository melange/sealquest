import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from quest_message import QuestMessage


class BotLogic:

    messages = dict()
    messages['bot_started'] = 'Bot started. Try /help to get help. Use /stop to stop'
    messages['bot_not_started'] = 'Bot is not running. Use /start to start the quest'
    messages['bot_stopped'] = 'Bot stopepd. Use /start to start the quest'
    messages['help'] = '/start - start bot\n/stop - stop bot\n/hint - ask for a hint\nTo answer a question send a message'
    messages['bot_is_already_runnings'] = 'Bot is already running. To stop use /stop'
    messages['answer_received'] = 'Answer received'

    def __init__(self, quest):
        if quest is None:
            raise AttributeError
        self.quest = quest
        self.is_started = False
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def handle_message(self, update, context):
        messages_list = list()

        if update is None:
            raise AttributeError
        if context is None:
            raise AttributeError

        if (update.message.text == "/start"):
            messages_list += self.start()
        elif (update.message.text == "/stop"):
            messages_list += self.stop()
        elif (update.message.text == "/help"):
            messages_list += self.help()
        elif (update.message.text == "/hint"):
            messages_list += self.hint()
        else:
            answer_text = update.message.text
            messages_list += self.answer(answer_text)
        
        self.send_messages(update, context, messages_list)


    def send_messages(self, update, context, messages_list):
        if update is None:
            raise AttributeError
        if context is None:
            raise AttributeError
        if messages_list is None:
            raise AttributeError


        chat_id = update.message.chat.id
        message_id = update.message.message_id

        if messages_list:
            for message in messages_list:
                if message.as_reply:
                    context.bot.send_message(chat_id, message.text, reply_to_message_id = message_id)
                else:
                    context.bot.send_message(chat_id, message.text)


    def start(self):
        messages_list = list()
        if self.is_started == False:
            self.is_started = True
            messages_list.append(QuestMessage(self.messages['bot_started'], False))
            messages_list += self.quest.start_quest()
        else:
            messages_list.append(QuestMessage(self.messages['bot_is_already_runnings'], False))
        return messages_list


    def stop(self):
        messages_list = list()
        if self.is_started == True:
            self.is_started = False
            self.quest.end_quest()
            messages_list.append(QuestMessage(self.messages['bot_stopped'], False))
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        return messages_list


    def help(self):
        messages_list = list()
        messages_list.append(QuestMessage(self.messages['help'], False))
        return messages_list


    def hint(self):
        messages_list = list()
        if self.is_started:
            messages_list += self.quest.get_hint()
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        return messages_list


    def answer(self, answer_text):
        messages_list = list()
        if self.is_started:
            messages_list += self.quest.assess_answer(answer_text)
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        return messages_list


    def error(self, update, context):
        messages_list = list()
        error_message = "Update caused error"
        messages_list.append(QuestMessage(error_message, False))
        self.logger.warning(error_message)
        return messages_list