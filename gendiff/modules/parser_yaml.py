__all__ = ['parser_yaml']

import yaml


def parser_yaml(filepath):
    with open(filepath, 'r') as data_dict:
        data = yaml.safe_load(data_dict)
    return data
