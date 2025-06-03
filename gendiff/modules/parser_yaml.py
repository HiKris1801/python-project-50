__all__ = ['parser_yaml']

import yaml


def parser_json(filepath):
    with open(filepath, 'r') as data_dict:
        data = yaml.load(data_dict)
    return data
