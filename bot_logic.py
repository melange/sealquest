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


    def __init__(self, quest):
        if quest is None:
            raise AttributeError
        self.quest = quest
        self.is_started = False
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def send_messages(self, update, context, messages_list):
        if messages_list:
            for message in messages_list:
                if message.as_reply:
                    update.message.reply_text(message.text)
                else:
                    context.bot.send_message(None, message.text)


    def start(self, update, context):
        messages_list = list()
        if self.is_started == False:
            self.is_started = True
            self.quest.start_quest()
            messages_list.append(QuestMessage(self.messages['bot_started'], False))
        else:
            messages_list.append(QuestMessage(self.messages['bot_is_already_runnings'], False))
        self.send_messages(update, context, messages_list)


    def stop(self, update, context):
        messages_list = list()
        if self.is_started == True:
            self.is_started = False
            self.quest.end_quest()
            messages_list.append(QuestMessage(self.messages['bot_stopped'], False))
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        self.send_messages(update, context, messages_list)


    def help(self, update, context):
        messages_list = list()
        messages_list.append(QuestMessage(self.messages['help'], False))
        self.send_messages(update, context, messages_list)


    def hint(self, update, context):
        messages_list = list()
        if self.is_started:
            messages_list += self.quest.get_hint()
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        self.send_messages(update, context, messages_list)


    def answer(self, update, context):
        messages_list = list()
        if self.is_started:
            answer = update.message
            messages_list += self.quest.assess_answer(answer)
        else:
            messages_list.append(QuestMessage(self.messages['bot_not_started'], False))
        self.send_messages(update, context, messages_list)


    def error(self, update, context):
        messages_list = list()
        error_message = "Update %s caused error %s" % update, context.error
        messages_list.append(QuestMessage(error_message, False))
        self.logger.warning(error_message)
        self.send_messages(update, context, messages_list)