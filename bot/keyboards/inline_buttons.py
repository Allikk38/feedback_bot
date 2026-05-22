# keyboards/inline_buttons.py
# Инлайн-клавиатуры

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    """Клавиатура для команды /start"""
    keyboard = [
        [InlineKeyboardButton("📋 Помощь", callback_data="help")],
        [InlineKeyboardButton("ℹ️ Информация", callback_data="info")],
        [InlineKeyboardButton("📝 Отправить отзыв", callback_data="feedback")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_help_keyboard():
    """Клавиатура для команды /help"""
    keyboard = [
        [InlineKeyboardButton("🏠 На главную", callback_data="start")],
        [InlineKeyboardButton("ℹ️ О боте", callback_data="info")]
    ]
    return InlineKeyboardMarkup(keyboard)
