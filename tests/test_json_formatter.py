import json

from gendiff.formatters.json_formatter import format_json


def test_format_json():
    diff_tree = {
        "key": "value",
        "changes": [
            {"type": "added", "key": "new_key", "value": "new_value"},
            {"type": "removed", "key": "old_key", "value": "old_value"},
        ],
    }
    expected_json = json.dumps(diff_tree, indent=4)
    assert format_json(diff_tree) == expected_json


def test_format_json_empty():
    diff_tree = {}
    expected_json = json.dumps(diff_tree, indent=4)
    assert format_json(diff_tree) == expected_json
