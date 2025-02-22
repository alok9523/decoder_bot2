from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import config
from handlers import convert, explain, run, admin, decode, optimize, syntax_checker

# Start command handler
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛠 Convert Code", callback_data="convert")],
        [InlineKeyboardButton("📖 Explain Code", callback_data="explain")],
        [InlineKeyboardButton("🚀 Run Code", callback_data="run")],
        [InlineKeyboardButton("🔧 Optimize Code", callback_data="optimize")],
        [InlineKeyboardButton("✅ Check Syntax", callback_data="syntax")],
        [InlineKeyboardButton("📜 Decode", callback_data="decode")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"""
🔥 *Advanced Code Helper Bot* 🔥  
👤 *Owner:* `{config.OWNER_NAME}`  
🔹 _Use the buttons below to access features._  
"""
    update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)

# Convert command
def convert_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Send me code with the format:\n`/convert <from_lang> <to_lang> <code>`", parse_mode="Markdown")

def process_convert(update: Update, context: CallbackContext):
    try:
        _, from_lang, to_lang, code = update.message.text.split(" ", 3)
        converted_code = convert.convert_code(code, from_lang, to_lang)
        update.message.reply_text(f"🔄 *Converted Code:*\n```{converted_code}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/convert <from_lang> <to_lang> <code>`", parse_mode="Markdown")

# Explain command
def explain_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Send me the code to explain:\n`/explain <code>`", parse_mode="Markdown")

def process_explain(update: Update, context: CallbackContext):
    try:
        _, code = update.message.text.split(" ", 1)
        explanation = explain.explain_code(code)
        update.message.reply_text(f"📖 *Explanation:*\n```{explanation}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/explain <code>`", parse_mode="Markdown")

# Run command
def run_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Send me the code to run:\n`/run <language> <code>`", parse_mode="Markdown")

def process_run(update: Update, context: CallbackContext):
    try:
        _, language, code = update.message.text.split(" ", 2)
        output = run.run_code(language, code)
        update.message.reply_text(f"🚀 *Output:*\n```{output}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/run <language> <code>`", parse_mode="Markdown")

# Optimize command
def process_optimize(update: Update, context: CallbackContext):
    try:
        _, code = update.message.text.split(" ", 1)
        optimized_code = optimize.optimize_code(code)
        update.message.reply_text(f"🔧 *Optimized Code:*\n```{optimized_code}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/optimize <code>`", parse_mode="Markdown")

# Syntax check command
def process_syntax(update: Update, context: CallbackContext):
    try:
        _, language, code = update.message.text.split(" ", 2)
        fixed_code = syntax_checker.check_syntax(code, language)
        update.message.reply_text(f"✅ *Fixed Code:*\n```{fixed_code}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/syntax <language> <code>`", parse_mode="Markdown")

# Decode command
def process_decode(update: Update, context: CallbackContext):
    try:
        _, encoding, text = update.message.text.split(" ", 2)
        if encoding.lower() == "base64":
            decoded_text = decode.decode_base64(text)
        elif encoding.lower() == "hex":
            decoded_text = decode.decode_hex(text)
        else:
            decoded_text = "❌ Unsupported encoding."
        update.message.reply_text(f"📜 *Decoded Text:*\n```{decoded_text}```", parse_mode="Markdown")
    except:
        update.message.reply_text("❌ *Error:* Invalid format. Use `/decode <base64|hex> <text>`", parse_mode="Markdown")

# Admin command
def admin_handler(update: Update, context: CallbackContext):
    admin.admin_command(update, context)

# Registering handlers
def main():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("convert", convert_handler))
    dp.add_handler(MessageHandler(Filters.regex(r"^/convert "), process_convert))
    dp.add_handler(CommandHandler("explain", explain_handler))
    dp.add_handler(MessageHandler(Filters.regex(r"^/explain "), process_explain))
    dp.add_handler(CommandHandler("run", run_handler))
    dp.add_handler(MessageHandler(Filters.regex(r"^/run "), process_run))
    dp.add_handler(CommandHandler("optimize", process_optimize))
    dp.add_handler(CommandHandler("syntax", process_syntax))
    dp.add_handler(CommandHandler("decode", process_decode))
    dp.add_handler(CommandHandler("admin", admin_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
