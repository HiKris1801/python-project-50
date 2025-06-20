import pytest

from gendiff.modules.parser_by_extension import get_parser_by_extension
from gendiff.modules.parser_json import parser_json
from gendiff.modules.parser_yaml import parser_yaml

fun_parser = get_parser_by_extension


def test_get_parser_by_extension_json():
    extension = ".json"

    assert fun_parser(extension) == parser_json


def test_get_parser_by_extension_yaml():
    extension = ".yaml"

    assert fun_parser(extension) == parser_yaml


def test_get_parser_by_extension_yml():
    extension = ".yml"

    assert fun_parser(extension) == parser_yaml


def test_get_parser_by_extension_raise():
    extension = ".txt"

    with pytest.raises(ValueError, match=f"Invalid file format: {extension}"):
        fun_parser(extension)
