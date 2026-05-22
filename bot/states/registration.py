# states/registration.py
# Состояния для ConversationHandler опроса пользователя

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from questions_config import QUESTIONS, MAX_ANSWER_LENGTH
import logging
from config import ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

# Состояния
ASKING_QUESTIONS = range(len(QUESTIONS))

# Хранилище ответов пользователей (в памяти)
user_answers = {}

async def start_survey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начать опрос - задать первый вопрос"""
    user_id = update.effective_user.id
    user_answers[user_id] = []
    
    question = QUESTIONS[0]
    await update.message.reply_text(question)
    return 0  # Первое состояние

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Обработать ответ и задать следующий вопрос"""
    user_id = update.effective_user.id
    answer = update.message.text.strip()
    
    # Проверка длины ответа
    if len(answer) > MAX_ANSWER_LENGTH:
        await update.message.reply_text(f"Ответ слишком длинный. Максимум {MAX_ANSWER_LENGTH} символов. Попробуйте ещё раз:")
        return context.user_data.get('current_question', 0)
    
    # Сохраняем ответ
    if user_id not in user_answers:
        user_answers[user_id] = []
    user_answers[user_id].append(answer)
    
    # Определяем текущий индекс вопроса
    current_idx = len(user_answers[user_id])
    
    # Проверяем, есть ли ещё вопросы
    if current_idx < len(QUESTIONS):
        next_question = QUESTIONS[current_idx]
        await update.message.reply_text(next_question)
        return current_idx
    else:
        # Все вопросы заданы - отправляем результаты администратору
        await send_results_to_admin(update, user_id)
        await update.message.reply_text("✅ Спасибо! Ваши ответы отправлены. Мы свяжемся с вами в ближайшее время.")
        
        # Очищаем данные пользователя
        if user_id in user_answers:
            del user_answers[user_id]
        
        return ConversationHandler.END

async def send_results_to_admin(update: Update, user_id: int):
    """Отправить собранные ответы администратору"""
    if user_id not in user_answers:
        return
    
    user = update.effective_user
    answers = user_answers[user_id]
    
    message = f"📝 Новый ответ на опрос\n\n"
    message += f"👤 Пользователь: @{user.username if user.username else 'нет username'} (ID: {user_id})\n"
    message += f"📅 Дата: {update.message.date.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    message += f"📋 Ответы:\n"
    
    for i, (question, answer) in enumerate(zip(QUESTIONS, answers), 1):
        message += f"\n{i}. {question}\n   → {answer}"
    
    try:
        await update.get_bot().send_message(chat_id=ADMIN_CHAT_ID, text=message[:4000])
        logger.info(f"Результаты опроса пользователя {user_id} отправлены администратору")
    except Exception as e:
        logger.error(f"Не удалось отправить результаты администратору: {e}")

async def cancel_survey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отменить опрос"""
    user_id = update.effective_user.id
    if user_id in user_answers:
        del user_answers[user_id]
    
    await update.message.reply_text("❌ Опрос отменен. Если передумаете, начните заново.")
    return ConversationHandler.END
