# feedback_bot
Создаю файл `README.md`:

```markdown
# Feedback Bot

Telegram-бот для сбора заявок и обратной связи.

## Структура проекта

```
feedback_bot/
├── bot/
│   ├── main.py                 # точка входа
│   ├── config.py               # конфигурация
│   ├── questions_config.py     # вопросы для опроса
│   ├── handlers/               # обработчики команд
│   ├── keyboards/              # клавиатуры
│   ├── utils/                  # вспомогательные функции
│   └── states/                 # состояния для опроса
├── requirements.txt            # зависимости
├── .env.example                # пример переменных окружения
├── .gitignore                  # исключения для git
└── README.md                   # инструкция
```

## Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и главное меню |
| `/help` | Список доступных команд |
| `/info` | Информация о боте |
| `/feedback <текст>` | Отправить отзыв администратору |
| `/survey` | Начать опрос |
| `/cancel` | Отменить опрос |

## Установка и запуск

### 1. Локально

```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/feedback_bot.git
cd feedback_bot

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Установить зависимости
pip install -r requirements.txt

# Создать файл .env из примера
cp .env.example .env

# Отредактировать .env - добавить BOT_TOKEN и ADMIN_CHAT_ID

# Запустить бота
cd bot
python main.py
```

### 2. На PythonAnywhere

1. Загрузить код через Files
2. В Bash-консоли установить зависимости:
   ```bash
   pip3 install --user -r requirements.txt
   ```
3. Создать файл `.env` с токеном и ADMIN_CHAT_ID
4. Запустить бота:
   ```bash
   cd bot && python3 main.py
   ```

## Переменные окружения (.env)

| Переменная | Описание |
|------------|----------|
| `BOT_TOKEN` | Токен бота от @BotFather |
| `ADMIN_CHAT_ID` | ID администратора для получения уведомлений |
| `LOG_LEVEL` | Уровень логирования (по умолчанию INFO) |

## Добавление новой команды

1. Создать файл в `handlers/`, например `new_command.py`
2. Реализовать функцию-обработчик
3. Импортировать в `handlers/__init__.py`
4. Добавить хендлер в `main.py`

## Изменение вопросов опроса

Отредактировать список `QUESTIONS` в файле `bot/questions_config.py`

## Лицензия

MIT
```
