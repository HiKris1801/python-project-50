import pytest

from gendiff.modules.file_parser import parse_file


def test_parse_file_json():
    file_path = 'tests/fixtures/sample.json'
    expected_data = {
        "name": "Alice",
        "age": 30,
        "active": True
    }
    assert parse_file(file_path) == expected_data


def test_parse_file_yaml():
    file_path = 'tests/fixtures/sample.yaml'
    expected_data = {
        "name": "Alice",
        "age": 30,
        "active": True
    }
    assert parse_file(file_path) == expected_data


def test_parse_file_invalid_extension(tmp_path):
    invalid_file = tmp_path / "data.txt"
    invalid_file.write_text("Just some text")

    with pytest.raises(ValueError, match="Invalid file format"):
        parse_file(str(invalid_file))
