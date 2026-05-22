# handlers/help.py
# Обработчик команды /help

from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline_buttons import get_help_keyboard
import logging

logger = logging.getLogger(__name__)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    user_id = update.effective_user.id
    
    logger.info(f"Пользователь {user_id} вызвал /help")
    
    help_text = (
        "📋 *Доступные команды:*\n\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение\n"
        "/info - Информация о боте\n"
        "/feedback <текст> - Отправить отзыв разработчику\n"
        "/survey - Начать опрос (подбор недвижимости)\n\n"
        "💡 *Совет:* Вы также можете использовать кнопки для быстрой навигации."
    )
    
    await update.message.reply_text(
        help_text,
        reply_markup=get_help_keyboard(),
        parse_mode='Markdown'
    )
