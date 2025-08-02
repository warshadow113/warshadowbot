
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # Убедись, что переменная окружения BOT_TOKEN задана

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я WarShadowBot. Следим за обстановкой.")

async def obstanovka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Следим за воздушной активностью и сообщим при опасности.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("obstanovka", obstanovka))

    print("Бот запущен. Ожидаем команды...")
    app.run_polling()

if __name__ == "__main__":
    main()
