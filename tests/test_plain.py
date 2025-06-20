from gendiff.formatters.plain import format_plain
from gendiff.modules.diff import generate_diff

fun_plain = format_plain


def test_format_plain_none_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': None,
            'path': 'common.setting'
        }
    ]

    expected_output = "Property 'setting' was added with value: null"

    assert fun_plain(diff) == expected_output


def test_format_plain_true_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': True,
            'path': 'common.setting'
        }
    ]

    expected_output = "Property 'setting' was added with value: true"

    assert fun_plain(diff) == expected_output


def test_format_plain_false_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': False,
            'path': 'common.setting'
        }
    ]

    expected_output = "Property 'setting' was added with value: false"

    assert fun_plain(diff) == expected_output


def test_format_plain_comlex_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': False,
            'path': 'common.setting'
        }
    ]

    expected_output = "Property 'setting' was added with value: false"

    assert fun_plain(diff) == expected_output


def est_plain_both_empty_dicts():
    diff = []

    expected_output = ''

    assert fun_plain(diff) == expected_output


def test_plain_first_empty_dict():
    dict1 = {}
    dict2 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'verbose': True
    }

    expected_output = (
        "Property 'host' was added with value: 'hexlet.io'\n"
        "Property 'timeout' was added with value: 50\n"
        "Property 'verbose' was added with value: true"
    )

    result = generate_diff(dict1, dict2, format_name='plain')
    assert result == expected_output


def test_plain_second_empty_dict():
    dict1 = {
        'host': 'hexlet.io'
    }
    dict2 = {}

    expected_output = (
        "Property 'host' was removed"
    )

    result = generate_diff(dict1, dict2, format_name='plain')
    assert result == expected_output


def test_plain_nested_added():
    dict1 = {
        "common": {
            "setting1": "Value 1"
        }
    }

    dict2 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200
        }
    }

    expected_output = "Property 'common.setting2' was added with value: 200"
    result = generate_diff(dict1, dict2, format_name='plain')
    assert result == expected_output


def test_plain_nested_removed():
    dict1 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200
        }
    }
    dict2 = {
        "common": {
            "setting1": "Value 1"
        }
    }

    expected_output = "Property 'common.setting2' was removed"
    result = generate_diff(dict1, dict2, format_name='plain')
    assert result == expected_output
