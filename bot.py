from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я MiniHouse-AI 🤖")

TOKEN = "os.getenv "

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен!")

app.run_polling()

