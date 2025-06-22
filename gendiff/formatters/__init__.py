from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

# Определяем имя форматера по умолчанию
DEFAULT_FORMATTER = 'stylish'

# Словарь, сопоставляющий имена форматеров с их функциями
FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def get_formatter(formatter_name):
    """
    Возвращает функцию форматирования по ее имени.
    Если имя не найдено, вызывает исключение.
    """
    if formatter_name not in FORMATTERS:
        raise ValueError(
            f"Неизвестный форматер: '{formatter_name}'. "
            f"Доступные форматеры: {', '.join(FORMATTERS.keys())}"
        )
    return FORMATTERS[formatter_name]
