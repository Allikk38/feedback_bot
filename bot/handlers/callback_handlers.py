# handlers/callback_handlers.py
# Обработчики callback-запросов от инлайн-кнопок

from telegram import Update
from telegram.ext import ContextTypes
import logging
from handlers.start import start_command
from handlers.help import help_command
from handlers.other import info_command

logger = logging.getLogger(__name__)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка нажатий на инлайн-кнопки"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    callback_data = query.data
    
    logger.info(f"Пользователь {user_id} нажал кнопку: {callback_data}")
    
    if callback_data == "start":
        await start_command(update, context)
    elif callback_data == "help":
        await help_command(update, context)
    elif callback_data == "info":
        await info_command(update, context)
    elif callback_data == "feedback":
        await query.edit_message_text(
            "📝 Отправьте ваш отзыв командой:\n"
            "/feedback Ваш текст здесь"
        )
    else:
        await query.edit_message_text("❌ Неизвестная команда")
