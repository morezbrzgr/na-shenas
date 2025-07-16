import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# فعال کردن لاگ‌ها برای دیباگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TELEGRAM_API_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! من ربات چت ناشناس هستم.')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('برای شروع چت، دستور /start رو بزنید.')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    # ساخت Updater با توکن
    updater = Updater(TOKEN, use_context=True)

    # دریافت دیسپاچر برای اضافه کردن هندلرها
    dispatcher = updater.dispatcher

    # اضافه کردن هندلرها
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
