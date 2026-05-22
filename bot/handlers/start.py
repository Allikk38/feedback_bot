# handlers/start.py
# Обработчик команды /start

from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline_buttons import get_start_keyboard
import logging

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    user = update.effective_user
    user_id = user.id
    username = user.username if user.username else "без username"
    
    logger.info(f"Пользователь {user_id} (@{username}) запустил /start")
    
    welcome_text = (
        f"👋 Здравствуйте, {user.first_name}!\n\n"
        f"Я помощник канала 'Горячие метры'\n"
        f"✨ Мой сервис помогает жителям Новосибирска и других регионов РФ "
        f"в подборе самых интересных объектов недвижимости\n\n"
        f"👉 Нажмите кнопку 'Помощь' для списка команд или начните опрос прямо сейчас."
    )
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=get_start_keyboard()
    )
