from pathlib import Path

__all__ = ['get_file_extension']  # Fixed typo: _all__ -> __all__


def get_file_extension(filepath):  # определение расширения файла
    file_path = Path(filepath)
    extension = file_path.suffix
    return extension


