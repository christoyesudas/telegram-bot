from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

# Store your bot token safely as an environment variable
TOKEN = os.getenv("BOT_TOKEN", "7812034748:AAHM3Ipty8E8N6OqoyLgp9bxEaEHODlEmWg")  # Replace with env variable in production

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome! Use:\n/movie - Type a movie name with the year.")

async def movie(update: Update, context: CallbackContext):
    await update.message.reply_text("Please type the name of the movie with the year (e.g., 'Inception 2010').")

async def handle_movie_name(update: Update, context: CallbackContext):
    movie_name = update.message.text  # Capture the movie name
    response_text = f"Movie: {movie_name}\nLink: https://tinyurl.com/25l4fzm7"
    await update.message.reply_text(response_text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("movie", movie))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_name))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
