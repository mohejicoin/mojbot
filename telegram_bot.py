import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("こんにちは！ボットが起動しました。")

def main() -> None:
    application = Application.builder().token("AAEd41L-4NKtakIQTXuGS3kgUXpxPr7XpGQ").build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
