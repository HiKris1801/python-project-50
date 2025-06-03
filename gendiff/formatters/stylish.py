def format_stylish(dict1, dict2):
    """
    Format the difference between two dictionaries in a stylish way.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        str: A string representing the difference in a stylish format.
    """
    result_diff = "{ \n"
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result_diff += f"  {key}: {dict1[key]}\n"
            else:
                result_diff += f"- {key}: {dict1[key]}\n"
                result_diff += f"+ {key}: {dict2[key]}\n"
        elif key in dict1:
            result_diff += f"- {key}: {dict1[key]}\n"
        elif key in dict2:
            result_diff += f"+ {key}: {dict2[key]}\n"
    result_diff += "} \n"
    return result_diff
