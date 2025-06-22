import json


def format_json(diff_tree):
    """
    Formats a diff_tree into a JSON string.
    """
    return json.dumps(diff_tree, indent=4)

