# handlers/other.py
# Обработчики остальных команд и эхо-режима

from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_CHAT_ID, BOT_VERSION, BOT_AUTHOR, BOT_REPO_URL
import logging

logger = logging.getLogger(__name__)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /info"""
    user_id = update.effective_user.id
    
    logger.info(f"Пользователь {user_id} вызвал /info")
    
    info_text = (
        f"🤖 *Информация о боте*\n\n"
        f"Версия: {BOT_VERSION}\n"
        f"Автор: {BOT_AUTHOR}\n"
        f"Проект: {BOT_REPO_URL}\n\n"
        f"Бот предназначен для сбора заявок и обратной связи."
    )
    
    await update.message.reply_text(info_text, parse_mode='Markdown')

async def feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /feedback <текст>"""
    user_id = update.effective_user.id
    user = update.effective_user
    username = user.username if user.username else "без username"
    
    # Получаем текст фидбека (все аргументы после команды)
    text = ' '.join(context.args)
    
    if not text:
        await update.message.reply_text(
            "❌ Вы не указали текст отзыва.\n"
            "Пример использования: `/feedback Ваш отзыв здесь`",
            parse_mode='Markdown'
        )
        return
    
    logger.info(f"Пользователь {user_id} отправил фидбек: {text[:50]}...")
    
    # Отправляем фидбек администратору
    feedback_message = (
        f"📝 *Новый отзыв*\n\n"
        f"👤 Пользователь: @{username} (ID: {user_id})\n"
        f"💬 Текст: {text}"
    )
    
    try:
        await update.get_bot().send_message(
            chat_id=ADMIN_CHAT_ID,
            text=feedback_message,
            parse_mode='Markdown'
        )
        await update.message.reply_text("✅ Спасибо за ваш отзыв! Мы его получили.")
        logger.info(f"Фидбек от пользователя {user_id} отправлен администратору")
    except Exception as e:
        logger.error(f"Не удалось отправить фидбек администратору: {e}")
        await update.message.reply_text(
            "⚠️ Произошла ошибка при отправке отзыва. Мы уже знаем и чиним."
        )

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Эхо-режим - ответ на неизвестные сообщения"""
    user_id = update.effective_user.id
    
    logger.info(f"Пользователь {user_id} отправил неизвестное сообщение: {update.message.text[:50]}")
    
    await update.message.reply_text(
        "🤔 Я вас не понял.\n\n"
        "Воспользуйтесь командой /help, чтобы увидеть список доступных команд."
    )
