# handlers/survey.py
# Обработчик команды /survey - запуск опроса

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from states.registration import start_survey, handle_answer, cancel_survey, ASKING_QUESTIONS
import logging

logger = logging.getLogger(__name__)

async def survey_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Запуск опроса"""
    user_id = update.effective_user.id
    
    logger.info(f"Пользователь {user_id} запустил опрос /survey")
    
    await update.message.reply_text(
        "📋 *Начинаем опрос*\n\n"
        "Пожалуйста, отвечайте на вопросы. Для отмены опроса отправьте /cancel",
        parse_mode='Markdown'
    )
    
    return await start_survey(update, context)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отмена опроса"""
    user_id = update.effective_user.id
    logger.info(f"Пользователь {user_id} отменил опрос")
    return await cancel_survey(update, context)
