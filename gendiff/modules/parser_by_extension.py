
from gendiff.modules.parser_json import parser_json
from gendiff.modules.parser_yaml import parser_yaml

__all__ = ['get_parser_by_extension']


def get_parser_by_extension(extension):
    if extension == ".json":
        return parser_json
    elif extension in (".yml", ".yaml"):
        return parser_yaml
    else:
        raise ValueError(f"Invalid file format: {extension}")
