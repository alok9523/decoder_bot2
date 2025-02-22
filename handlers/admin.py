from telegram import Update
from telegram.ext import CallbackContext
import config

ADMIN_IDS = [123456789]  # Replace with actual Telegram Admin IDs

def is_admin(user_id):
    """Check if a user is an admin."""
    return user_id in ADMIN_IDS

def admin_command(update: Update, context: CallbackContext):
    """Handles admin-only commands."""
    user_id = update.effective_user.id
    if is_admin(user_id):
        update.message.reply_text("Admin command executed successfully.")
    else:
        update.message.reply_text("You are not authorized to use this command.")
