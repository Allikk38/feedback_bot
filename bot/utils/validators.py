# utils/validators.py
# Вспомогательные функции для проверки ввода

def validate_feedback_length(text: str, max_length: int = 1000) -> bool:
    """Проверяет, что длина фидбека не превышает максимум"""
    return len(text) <= max_length

def sanitize_text(text: str) -> str:
    """Очищает текст от лишних пробелов и символов"""
    if not text:
        return ""
    return text.strip()[:4000]  # Ограничиваем длину сообщения
