def generate_diff(dict1, dict2):
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
                nested_diff = generate_diff(val1, val2)
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
