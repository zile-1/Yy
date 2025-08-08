from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hello, कैसे हैं आप?')

def respond(update, context):
    text = update.message.text.lower()
    if 'क्या कर रहे हो' in text:
        update.message.reply_text('मैं तुम्हारी मदद कर रहा हूँ!')
    elif 'कैसे हो' in text:
        update.message.reply_text('मैं बढ़िया हूँ, तुम बताओ!')
    else:
        update.message.reply_text('मुझे समझ नहीं आया, कुछ और पूछो!')

def main():
    updater = Updater("7839163239:AAHagtBWiORmaMRhun262s_hybeT4oeL1WI", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
