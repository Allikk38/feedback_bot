# main.py
# Точка входа в приложение

import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ConversationHandler
from config import BOT_TOKEN
from handlers import (
    start_command, help_command, info_command, feedback_command, echo_handler,
    survey_command, cancel, handle_callback
)
from states.registration import handle_answer, ASKING_QUESTIONS
from utils.logger import setup_logger
import logging

# Настройка логгера
logger = setup_logger()

async def error_handler(update, context):
    """Глобальный обработчик ошибок"""
    logger.error(f"Произошла ошибка: {context.error}", exc_info=True)
    
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "⚠️ Произошла ошибка. Мы уже знаем и чиним."
        )

def main():
    """Запуск бота"""
    logger.info("Запуск бота...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("feedback", feedback_command))
    
    # ConversationHandler для опроса
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("survey", survey_command)],
        states={
            state: MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer)
            for state in ASKING_QUESTIONS
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    application.add_handler(conv_handler)
    
    # Обработчик инлайн-кнопок
    application.add_handler(CallbackQueryHandler(handle_callback))
    
    # Эхо-режим (на любое текстовое сообщение, не являющееся командой)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    
    # Глобальный обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота в режиме polling
    logger.info("Бот запущен и готов к работе")
    application.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
