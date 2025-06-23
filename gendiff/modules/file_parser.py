from gendiff.modules.file_extension import get_file_extension
from gendiff.modules.parser_by_extension import get_parser_by_extension


def parse_file(filepath):
    """Парсит файл и возвращает словарь."""
    extension = get_file_extension(filepath)
    parser = get_parser_by_extension(extension)
    return parser(filepath)
