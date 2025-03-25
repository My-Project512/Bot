import os
import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "8083859948:AAEO-dqwRaUVyUUueXUizwbcMMqTgQ3wsl4"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("मुझे कोई भी वीडियो लिंक भेजें, और मैं उसे डाउनलोड करके आपको भेज दूँगा।")

async def download_video(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    await update.message.reply_text("वीडियो डाउनलोड किया जा रहा है, कृपया प्रतीक्षा करें...")

    # yt-dlp का उपयोग करके वीडियो डाउनलोड करें
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        
        with open("video.mp4", "rb") as video:
            await update.message.reply_video(video=video)

        os.remove("video.mp4")  # वीडियो भेजने के बाद डिलीट कर दें
    except Exception as e:
        await update.message.reply_text(f"डाऊनलोड में समस्या आई: {str(e)}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    app.run_polling()

if __name__ == "__main__":
    main()