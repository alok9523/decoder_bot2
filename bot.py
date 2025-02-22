from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import config
from handlers import convert, explain, run, admin, decode, optimize, syntax_checker
from handlers.convert import convert_code
from handlers.explain import explain_code
from handlers.run import run_code
from handlers.optimize import optimize_code
from handlers.syntax_checker import check_syntax
from handlers.decode import decode_base64, decode_hex
from handlers.admin import admin_command

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)

# Handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    responses = {
        "convert": "Send me code with `/convert <from_lang> <to_lang> <code>`",
        "explain": "Send me code with `/explain <code>`",
        "run": "Send me code with `/run <language> <code>`",
        "optimize": "Send me code with `/optimize <code>`",
        "syntax": "Send me code with `/syntax <language> <code>`",
        "decode": "Send me code with `/decode <base64|hex> <text>`",
    }
    
    if data in responses:
        await query.message.reply_text(responses[data])

async def process_convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, from_lang, to_lang, code = update.message.text.split(" ", 3)
        converted_code = await convert_code(code, from_lang, to_lang)
        await update.message.reply_text(f"🔄 *Converted Code:*\n```{converted_code}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/convert <from_lang> <to_lang> <code>`", parse_mode="Markdown")
async def process_explain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, code = update.message.text.split(" ", 1)
        explanation = await explain_code(code)
        await update.message.reply_text(f"📖 *Explanation:*\n```{explanation}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/explain <code>`", parse_mode="Markdown")      

async def process_run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, language, code = update.message.text.split(" ", 2)
        output = await run_code(language, code)
        await update.message.reply_text(f"🚀 *Output:*\n```{output}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/run <language> <code>`", parse_mode="Markdown")
        
async def process_optimize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, code = update.message.text.split(" ", 1)
        optimized_code = await optimize_code(code)
        await update.message.reply_text(f"🔧 *Optimized Code:*\n```{optimized_code}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/optimize <code>`", parse_mode="Markdown")async def process_syntax(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, language, code = update.message.text.split(" ", 2)
        fixed_code = await check_syntax(code, language)
        await update.message.reply_text(f"✅ *Fixed Code:*\n```{fixed_code}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/syntax <language> <code>`", parse_mode="Markdown")
        
async def process_decode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, encoding, text = update.message.text.split(" ", 2)
        if encoding.lower() == "base64":
            decoded_text = await decode_base64(text)
        elif encoding.lower() == "hex":
            decoded_text = await decode_hex(text)
        else:
            decoded_text = "❌ Unsupported encoding."
        await update.message.reply_text(f"📜 *Decoded Text:*\n```{decoded_text}```", parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ *Error:* Invalid format. Use `/decode <base64|hex> <text>`", parse_mode="Markdown")
       
qasync def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await admin_command(update, context)

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("convert", process_convert))
    app.add_handler(CommandHandler("explain", process_explain))
    app.add_handler(CommandHandler("run", process_run))
    app.add_handler(CommandHandler("optimize", process_optimize))
    app.add_handler(CommandHandler("syntax", process_syntax))
    app.add_handler(CommandHandler("decode", process_decode))
    app.add_handler(CommandHandler("admin", admin_handler))

    # Register callback query handler for buttons
    app.add_handler(CallbackQueryHandler(button_click))

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()
