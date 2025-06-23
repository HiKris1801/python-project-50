import json

from gendiff.modules.diff import generate_diff


def test_generate_diff_stylish_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    result = generate_diff(file1, file2, format_name="stylish")
    assert result.strip() == expected.strip()


def test_generate_diff_plain_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'

    expected = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

    result = generate_diff(file1, file2, format_name="plain")
    assert result.strip() == expected.strip()


def test_generate_diff_json_output():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result = generate_diff(file1, file2, format_name="json")

    # Проверяем, что это валидный JSON
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    assert all('key' in item for item in parsed)
