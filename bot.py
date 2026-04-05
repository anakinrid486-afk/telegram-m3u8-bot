import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8480445544:AAG4ZWfKwXa7cqFPDItN4w1wtg4Yb8oKxlM"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    if ".m3u8" in url:
        await update.message.reply_text("Descargando...")

        os.system(f'ffmpeg -i "{url}" -c copy video.mp4')

        await update.message.reply_video(video=open("video.mp4", "rb"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
