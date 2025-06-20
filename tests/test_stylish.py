import pytest

from gendiff.formatters.stylish import format_stylish

fun_stylish = format_stylish


def test_format_stylish_unchanged_key():
    diff = [
        {
            'key': 'name',
            'status': 'unchanged',
            'value': 'Alice'
        }
    ]

    expected_output = '''{
    name: Alice
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_added_key():
    diff = [
        {
            'key': 'name',
            'status': 'added',
            'value': 'Alice'
        }
    ]

    expected_output = '''{
  + name: Alice
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_removed_key():
    diff = [
        {
            'key': 'name',
            'status': 'removed',
            'value': 'Alice'
        }
    ]

    expected_output = '''{
  - name: Alice
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_change_key():
    diff = [
        {
            'key': 'timeout',
            'status': 'changed',
            'old_val': 50,
            'new_val': 20
        }
    ]

    expected_output = '''{
  - timeout: 50
  + timeout: 20
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_nested_block():
    diff = [
        {
            'key': 'common',
            'status': 'nested',
            'children': [
                {'key': 'setting1', 'status': 'unchanged', 'value': 'Value 1'},
                {'key': 'setting2', 'status': 'removed', 'value': 200},
                {'key': 'setting3', 'status': 'added', 'value': True}
            ]
        }
    ]

    expected_output = '''{
    common: {
        setting1: Value 1
      - setting2: 200
      + setting3: true
    }
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_none_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': None
        }
    ]

    expected_output = '''{
  + setting: null
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_bool_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': True
        }
    ]

    expected_output = '''{
  + setting: true
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_bools_value():
    diff = [
        {
            'key': 'setting',
            'status': 'added',
            'value': False
        }
    ]

    expected_output = '''{
  + setting: false
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_booleans_and_null():
    diff = [
        {
            'key': 'flag',
            'status': 'changed',
            'old_val': True,
            'new_val': False
        },
        {
            'key': 'option',
            'status': 'changed',
            'old_val': None,
            'new_val': False
        },
        {
            'key': 'is_active',
            'status': 'unchanged',
            'value': True
        },
        {
            'key': 'debug',
            'status': 'added',
            'value': None
        }
    ]

    expected_output = '''{
  - flag: true
  + flag: false
  - option: null
  + option: false
    is_active: true
  + debug: null
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_sorted():
    diff = [
        {
            'key': 'a',
            'status': 'unchanged',
            'value': 2
        },
        {
            'key': 'b',
            'status': 'added',
            'value': 1
        },
        {
            'key': 'c',
            'status': 'removed',
            'value': 3
        }
    ]

    expected_output = '''{
    a: 2
  + b: 1
  - c: 3
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_all_values():
    diff = [
        {
            'key': 'flag',
            'status': 'changed',
            'old_val': True,
            'new_val': False
        },
        {
            'key': 'option',
            'status': 'changed',
            'old_val': None,
            'new_val': False
        },
        {
            'key': 'is_active',
            'status': 'unchanged',
            'value': True
        },
        {
            'key': 'debug',
            'status': 'changed',
            'old_val': 17,
            'new_val': 'object 1'
        }
    ]

    expected_output = '''{
  - flag: true
  + flag: false
  - option: null
  + option: false
    is_active: true
  - debug: 17
  + debug: object 1
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_unknown_status():
    diff = [
        {
            'key': 'unknown_key',
            'status': 'unexpected_status',
            'value': 'some value'
        }
    ]

    with pytest.raises(ValueError, match="Unknown status: unexpected_status"):
        fun_stylish(diff)


def test_format_stylish_empty():
    diff = []

    expected_output = '''{
}'''

    assert fun_stylish(diff) == expected_output


def test_format_stylish_none_value_unchanged():
    diff = [
        {
            'key': 'example',
            'status': 'unchanged',
            'value': None
        }
    ]

    expected_output = '''{
    example: null
}'''

    assert fun_stylish(diff) == expected_output

