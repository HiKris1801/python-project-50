from gendiff.formatters.plain import format_plain
from gendiff.modules.diff import build_diff_tree


def test_format_plain_none_value():
    diff = [{
        'key': 'setting',
        'status': 'added',
        'value': None
    }]
    assert format_plain(diff) == "Property 'setting' was added with value: null"


def test_format_plain_true_value():
    diff = [{
        'key': 'setting',
        'status': 'added',
        'value': True
    }]
    assert format_plain(diff) == "Property 'setting' was added with value: true"


def test_format_plain_false_value():
    diff = [{
        'key': 'setting',
        'status': 'added',
        'value': False
    }]
    assert format_plain(diff) == (
        "Property 'setting' was added with value: false"
    )


def test_format_plain_empty_diff():
    diff = []
    assert format_plain(diff) == ""


def test_plain_first_empty_dict():
    dict1 = {}
    dict2 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'verbose': True
    }

    expected = (
        "Property 'host' was added with value: 'hexlet.io'\n"
        "Property 'timeout' was added with value: 50\n"
        "Property 'verbose' was added with value: true"
    )

    result = format_plain(build_diff_tree(dict1, dict2))
    assert result == expected


def test_plain_second_empty_dict():
    dict1 = {'host': 'hexlet.io'}
    dict2 = {}

    expected = "Property 'host' was removed"
    result = format_plain(build_diff_tree(dict1, dict2))
    assert result == expected


def test_plain_nested_added():
    dict1 = {"common": {"setting1": "Value 1"}}
    dict2 = {"common": {"setting1": "Value 1", "setting2": 200}}

    expected = "Property 'common.setting2' was added with value: 200"
    result = format_plain(build_diff_tree(dict1, dict2))
    assert result == expected


def test_plain_nested_removed():
    dict1 = {"common": {"setting1": "Value 1", "setting2": 200}}
    dict2 = {"common": {"setting1": "Value 1"}}

    expected = "Property 'common.setting2' was removed"
    result = format_plain(build_diff_tree(dict1, dict2))
    assert result == expected
