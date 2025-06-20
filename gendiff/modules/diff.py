from gendiff.formatters import DEFAULT_FORMATTER, get_formatter


def build_diff_tree(dict1, dict2):
    diff_list = []
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    if not all_keys:
        return diff_list

    for key in all_keys:
        val1 = dict1.get(key)
        val2 = dict2.get(key)

        # если ключ есть в обоих словарях
        if key in dict1 and key in dict2:
            # если оба значения — словари, сравниваем рекурсивно
            if isinstance(val1, dict) and isinstance(val2, dict):
                nested_diff = build_diff_tree(val1, val2)
                diff_list.append({
                    "key": key,
                    "status": "nested",
                    "children": nested_diff
                })

            # если значения равны
            elif val1 == val2:
                diff_list.append({
                    "key": key,
                    "status": "unchanged",
                    "value": val1
                })

            # если значения разные
            else:
                diff_list.append({
                    "key": key,
                    "status": "changed",
                    "old_val": val1,
                    "new_val": val2
                })

        # если ключ только в dict1
        elif key in dict1:
            diff_list.append({
                "key": key,
                "status": "removed",
                "value": val1
            })

        # если ключ только в dict2
        else:  # key in dict2
            diff_list.append({
                "key": key,
                "status": "added",
                "value": val2
            })

    return diff_list


def generate_diff(dict1, dict2, format_name=DEFAULT_FORMATTER):
    """
    Compares two dictionaries, builds a difference tree and formats it.

    Arguments:
    dict1 (dict): The first dictionary to compare.
    dict2 (dict): The second dictionary to compare.
    format_name (str): The name of the desired output format
    (defaults to 'styli
sh').
    Returns:
    str: A formatted string representing the difference.
    """
    # 1. Строим дерево различий, используя переименованную функцию
    diff_tree = build_diff_tree(dict1, dict2)

    # 2. Получаем функцию форматирования по имени
    formatter_function = get_formatter(format_name)

    # 3. Форматируем дерево различий
    formatted_output = formatter_function(diff_tree)

    return formatted_output
