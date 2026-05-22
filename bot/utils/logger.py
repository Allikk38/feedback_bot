# utils/logger.py
# Настройка логирования

import logging
import sys
from config import LOG_LEVEL

def setup_logger():
    """Настройка и возврат корневого логгера"""
    
    # Получаем уровень логирования из конфига
    log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    
    # Создаем форматтер
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Создаем обработчик для вывода в консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Настраиваем корневой логгер
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)
    
    return root_logger
