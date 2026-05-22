# config.py
# Конфигурация бота и переменные окружения

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла (для локальной разработки)
load_dotenv()

# Токен бота, полученный от @BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ID администратора для получения фидбеков и логов ошибок
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

# Уровень логирования (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Версия бота
BOT_VERSION = "1.0.0"

# Автор бота
BOT_AUTHOR = "Разработчик"

# Ссылка на проект (если есть)
BOT_REPO_URL = "https://github.com/example/feedback_bot"

# Проверка обязательных переменных
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")

if not ADMIN_CHAT_ID:
    raise ValueError("ADMIN_CHAT_ID не найден в переменных окружения")

# Преобразуем ADMIN_CHAT_ID в int (Telegram ожидает число)
try:
    ADMIN_CHAT_ID = int(ADMIN_CHAT_ID)
except ValueError:
    raise ValueError("ADMIN_CHAT_ID должен быть числом")
