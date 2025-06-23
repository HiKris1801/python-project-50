from gendiff.modules.diff import build_diff_tree

fun_diff = build_diff_tree


def test_empty_dict():
    """ Test case for two empty dictionaries. """
    dict1 = {}
    dict2 = {}
    expected_diff = []

    assert fun_diff(dict1, dict2) == expected_diff


def test_two_dicts_status():
    """ Test case for two  dictionaries. """
    dict1 = {'key': 'value'}
    dict2 = {}
    expected_diff = [{'key': 'key', 'status': 'removed', 'value': 'value'}]

    assert fun_diff(dict1, dict2) == expected_diff


def test_two_dicts():
    """ Test case for two  dictionaries. """
    dict1 = {}
    dict2 = {'key1': 'value1', 'key2': 'value2'}
    expected_diff = [
    {'key': 'key1', 'status': 'added', 'value': 'value1'},
    {'key': 'key2', 'status': 'added', 'value': 'value2'}
]

    assert fun_diff(dict1, dict2) == expected_diff


def test_identical_dict():
    """ Test case for two identical dictionaries. """
    dict1 = {'key1': 'value1', 'key2': 'value2'}
    dict2 = {'key1': 'value1', 'key2': 'value2'}
    expected_diff = [{'key': 'key1', 'status': 'unchanged', 'value': 'value1'},
                     {'key': 'key2', 'status': 'unchanged', 'value': 'value2'}]

    assert fun_diff(dict1, dict2) == expected_diff


def test_del_key():
    """ Test case for deleting a key from the first dictionary. """
    dict1 = {'key1': 'value1'}
    dict2 = {}
    expected_diff = [{'key': 'key1', 'status': 'removed', 'value': 'value1'}]

    assert fun_diff(dict1, dict2) == expected_diff


def test_change_keys():
    """ Test case for changing a key in the second dictionary. """
    dict1 = {'x': 1}
    dict2 = {'x': 2}
    expected_diff = [
        {'key': 'x', 'status': 'changed', 'old_val': 1, 'new_val': 2}
    ]
    assert fun_diff(dict1, dict2) == expected_diff


def test_some_keys():
    """ Test case for dictionaries with some common and some different keys. """
    dict1 = {'x': 1, 'y': 2}
    dict2 = {'x': 1, 'y': 3}
    expected_diff = [
        {'key': 'x', 'status': 'unchanged', 'value': 1},
        {'key': 'y', 'status': 'changed', 'old_val': 2, 'new_val': 3}
    ]

    assert fun_diff(dict1, dict2) == expected_diff


def test_sort_keys():
    """ Test case for dictionaries with unsorted keys. """
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'c': 3}
    expected_diff = [
        {'key': 'a', 'status': 'unchanged', 'value': 1},
        {'key': 'b', 'status': 'removed', 'value': 2},
        {'key': 'c', 'status': 'added', 'value': 3}
    ]
    assert fun_diff(dict1, dict2) == expected_diff


def test_type_object():

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'c': 3}
    expected_diff = [
        {'key': 'a', 'status': 'unchanged', 'value': 1},
        {'key': 'b', 'status': 'removed', 'value': 2},
        {'key': 'c', 'status': 'added', 'value': 3}
    ]

    assert fun_diff(dict1, dict2) == expected_diff


def test_mixed_types():
    """Test case where one value is a dict and the other is not."""
    dict1 = {'key': {'a': 1}}
    dict2 = {'key': 42}
    expected_diff = [
        {'key': 'key', 'status': 'changed', 'old_val': {'a': 1}, 'new_val': 42}
    ]

    assert fun_diff(dict1, dict2) == expected_diff


def test_nested_dicts():
    """Test case for nested dictionaries."""
    dict1 = {'parent': {'child': 1}}
    dict2 = {'parent': {'child': 2}}

    expected_diff = [
        {
            'key': 'parent',
            'status': 'nested',
            'children': [
                {'key': 'child',
                'status': 'changed',
                'old_val': 1,
                'new_val': 2}
            ]
        }
    ]

    assert fun_diff(dict1, dict2) == expected_diff


def test_none_and_bool_values():
    """Test case for None and boolean values."""
    dict1 = {'a': None, 'b': True, 'c': False}
    dict2 = {'a': None, 'b': False, 'c': False}

    expected_diff = [
        {'key': 'a', 'status': 'unchanged', 'value': None},
        {'key': 'b', 'status': 'changed', 'old_val': True, 'new_val': False},
        {'key': 'c', 'status': 'unchanged', 'value': False}
    ]

    assert fun_diff(dict1, dict2) == expected_diff
