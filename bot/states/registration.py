from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from questions_config import QUESTIONS
import logging
from config import ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

async def start_survey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начать опрос"""
    context.user_data['answers'] = []
    await update.message.reply_text(QUESTIONS[0])
    return 0

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Обработать ответ"""
    answer = update.message.text.strip()
    answers = context.user_data.get('answers', [])
    current_idx = len(answers)
    
    answers.append(answer)
    context.user_data['answers'] = answers
    
    next_idx = current_idx + 1
    
    if next_idx < len(QUESTIONS):
        await update.message.reply_text(QUESTIONS[next_idx])
        return next_idx
    else:
        await send_results_to_admin(update, context)
        await update.message.reply_text("✅ Спасибо! Ваши ответы отправлены.")
        context.user_data.clear()
        return ConversationHandler.END

async def send_results_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправить результаты администратору"""
    user = update.effective_user
    answers = context.user_data.get('answers', [])
    
    if not answers:
        return
    
    message = f"📝 Новый ответ на опрос\n\n"
    message += f"👤 Пользователь: @{user.username if user.username else 'нет username'} (ID: {user.id})\n\n"
    message += f"📋 Ответы:\n"
    
    for i, (question, answer) in enumerate(zip(QUESTIONS, answers), 1):
        message += f"\n{i}. {question}\n   → {answer}"
    
    try:
        await update.get_bot().send_message(chat_id=ADMIN_CHAT_ID, text=message[:4000])
        logger.info(f"Результаты опроса пользователя {user.id} отправлены")
    except Exception as e:
        logger.error(f"Ошибка отправки: {e}")

async def cancel_survey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отменить опрос"""
    context.user_data.clear()
    await update.message.reply_text("❌ Опрос отменен.")
    return ConversationHandler.END
