from telegram import Bot
from telegram.ext import Updater, CommandHandler
from credits import bot_token
import math

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, '''Привет! Напиши /help, чтобы узнать возможности бота''')

def help(update, context):
    context.bot.send_message(update.effective_chat.id, '''/fct [число] - факториал введенного числа
/sqrt [число] - квадратный корень введенного числа
/round [число] - округленние введенного числа до ближайшего большего числа
/pi - выведение числа пи
/e - выведение числа Эйлера
/log [число] - логарифм по основанию 2''')

def fct(update, context):
    msg = " ".join(context.args)
    msg = int(msg)
    update.message.reply_text(math.factorial(msg))

def sqrt(update, context):
    msg = " ".join(context.args)
    msg = int(msg)
    update.message.reply_text(math.sqrt(msg))

def round(update, context):
    msg = " ".join(context.args)
    msg = float(msg)
    update.message.reply_text(math.ceil(msg))

def pi(update, context):
    context.bot.send_message(update.effective_chat.id, math.pi)

def e(update, context):
    context.bot.send_message(update.effective_chat.id, math.e)

def log(update, context):
    msg = " ".join(context.args)
    msg = int(msg)
    update.message.reply_text(math.log2(msg))

start_handler = CommandHandler('start', start)
fct_handler = CommandHandler('fct', fct)
round_handler = CommandHandler('round', round)
help_handler = CommandHandler('help', help)
sqrt_handler = CommandHandler('sqrt', sqrt)
pi_handler = CommandHandler('pi', pi)
log_handler = CommandHandler('log', log)
e_handler = CommandHandler('e', e)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(fct_handler)
dispatcher.add_handler(round_handler)
dispatcher.add_handler(sqrt_handler)
dispatcher.add_handler(pi_handler)
dispatcher.add_handler(log_handler)
dispatcher.add_handler(e_handler)

updater.start_polling()
updater.idle()
