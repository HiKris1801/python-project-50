
from pathlib import Path


_all__ = ['get_file_extension']


def get_file_extension(filepath): # определение расширения файла
    file_path = Path(filepath)
    extension = file_path.suffix
    return extension


