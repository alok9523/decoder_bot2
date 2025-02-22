import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import config

# Logging setup
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Function to query GPT-4o
def ask_gpt4o(prompt):
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Command: Start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am an AI-powered coding assistant. Send me your code-related questions!")

# Handle user messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = ask_gpt4o(user_input)
    update.message.reply_text(response)

# Main function
def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Commands
    dp.add_handler(CommandHandler("start", start))
    
    # Messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
