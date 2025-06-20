from gendiff.modules.parser_json import parser_json


def test_parser_json():
    filepath = 'tests/tests_data/json/file1.json'
    expected_data = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }

    assert parser_json(filepath) == expected_data
