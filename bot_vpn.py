from flask import Flask
from threading import Thread
import telebot
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()

TOKEN = "8521576609:AAE06Bt3K5CFc1HoBV6IWrmfpkTiS4AWJiA"
bot = telebot.TeleBot(TOKEN)

HELP_TEXT = "DANH SÁCH LỆNH HỖ TRỢ:\n/help : Danh sách lệnh hỗ trợ"

@bot.message_handler(commands=["notes"])
def notes_command(message):
    bot.reply_to(message, HELP_TEXT)

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, HELP_TEXT)

if __name__ == "__main__":
    keep_alive()
    print("Bot đang khởi động...")
    bot.remove_webhook()  # đảm bảo polling không bị webhook chặn
    bot.infinity_polling(skip_pending=True, timeout=30, long_polling_timeout=30)
