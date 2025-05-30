from gendiff.modules.diff import generate_diff

fun_diff = generate_diff

def test_empty_dict():
    dict1 = {}
    dict2 = {}
    expected_diff = "{ \n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_identical_dict():
    dict1 = {'key1': 'value1', 'key2': 'value2'}
    dict2 = {'key1': 'value1', 'key2': 'value2'}
    expected_diff = "{ \n  key1: value1\n  key2: value2\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_add_key():
    dict1 = {}
    dict2 = {'key1': 'value1'}
    expected_diff = "{ \n+ key1: value1\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_del_key():
    dict1 = {'key1': 'value1'}
    dict2 = {}
    expected_diff = "{ \n- key1: value1\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_change_keys():
    dict1 = {'x': 1}
    dict2 = {'x': 2}
    expected_diff = "{ \n- x: 1\n+ x: 2\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_some_keys():
    dict1 = {'x': 1, 'y': 2}
    dict2 = {'x': 1, 'y': 3}
    expected_diff = "{ \n  x: 1\n- y: 2\n+ y: 3\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff

def test_sort_keys():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'c': 3}
    expected_diff = "{ \n  a: 1\n- b: 2\n+ c: 3\n} \n"

    assert fun_diff(dict1, dict2) == expected_diff


