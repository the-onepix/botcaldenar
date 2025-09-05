from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/")
def index():
    return "Bot is running!"

# Обработчик команды
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет 👋 Выберите дату для бронирования:",
        reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).row("📅 06.09", "📅 07.09", "📅 08.09")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
