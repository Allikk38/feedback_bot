# keyboards/__init__.py
# Инициализация модуля keyboards

from .inline_buttons import get_start_keyboard, get_help_keyboard

__all__ = [
    'get_start_keyboard',
    'get_help_keyboard'
]
