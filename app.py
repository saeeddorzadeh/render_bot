import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "ربات زنده است!"

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("سلام! ربات روی Render روشن شد.")

def run_bot():
    token = "7504872864:AAGEOAB99ZH8Yu6dbSC3HBQ32XOiU9vjhho"
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if ___name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)