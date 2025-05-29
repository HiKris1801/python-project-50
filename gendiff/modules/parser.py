__all__ = ['parser_json']

import json


def parser_json(filepath):
    with open(filepath, 'r') as data_dict:
        data = json.load(data_dict)
    return data
