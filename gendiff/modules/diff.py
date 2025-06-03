from gendiff.modules.file_extension import get_file_extension

from gendiff.modules.parser_by_extension import get_parser_by_extension
from gendiff.modules import parser_json, parser_yaml


_all__ = ['generate_diff']


def generate_diff(filepath1, filepath2):
    ext1 = get_file_extension(filepath1)
    ext2 = get_file_extension(filepath2)
    parser1 = get_parser_by_extension(ext1)
    parser2 = get_parser_by_extension(ext2)

    dict1 = parser1(filepath1)
    dict2 = parser2(filepath2)
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result_diff += {key}: {dict1[key]}
            else:
                result_diff += f"- {key}: {dict1[key]}\n"
                result_diff += f"+ {key}: {dict2[key]}\n"
        elif key in dict1:
            result_diff += f"- {key}: {dict1[key]}\n"
        elif key in dict2:
            result_diff += f"+ {key}: {dict2[key]}\n"
    result_diff += "} \n"
    return result_diff





