from gendiff.modules.file_extension import get_file_extension


def test_get_file_extension():
    assert get_file_extension('file.json') == '.json'
    assert get_file_extension('file.yaml') == '.yaml'
    assert get_file_extension('file.yml') == '.yml'
    assert get_file_extension('file.txt') == '.txt'
    assert get_file_extension('file') == ''

