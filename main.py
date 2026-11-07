import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "⚓ أهلاً بك في CAPTAIN\n\n"
        "نظام تيليغرام المتكامل.\n"
        "اكتب /help لعرض الأوامر."
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "⚓ CAPTAIN\n\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n"
        "/status - حالة البوت"
    )

@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, "🟢 CAPTAIN يعمل بنجاح.")

bot.infinity_polling()
