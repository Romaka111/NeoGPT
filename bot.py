import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import nest_asyncio

BOT_TOKEN = "7584731929:AAEV05mjsHb_7wl6eqkDwP1yfQ09o2ciklI"
BASE_URL = os.environ.get("BASE_URL","https://web-production-6325f.up.railway.app")
WEBHOOK_SECRET_KEY = os.environ.get("WEBHOOK_SECRET_KEY","supersecret")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это NeoGPT, я запущен на Webhook с защитой!")

async def start_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    webhook_url = f"{BASE_URL}/webhook/{WEBHOOK_SECRET_KEY}"
    await app.bot.set_webhook(url=webhook_url, secret_token=WEBHOOK_SECRET_KEY)
    print("Webhook установлен с секретом:", webhook_url)

    await app.run_webhook(
        listen="0.0.0.0",
        port=8000,
        webhook_path=f"/webhook/{WEBHOOK_SECRET_KEY}"
    )

if __name__ == "__main__":
    asyncio.run(start_bot())
