from gendiff.modules.parser_yaml import parser_yaml


def test_parser_yaml():
    filepath = 'tests/tests_data/yaml/file1.yaml'
    expected_data = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}

    assert parser_yaml(filepath) == expected_data
