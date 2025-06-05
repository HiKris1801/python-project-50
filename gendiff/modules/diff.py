def generate_diff(dict1, dict2):
    diff_list = []
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    if not all_keys:
        return diff_list
    for key in all_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                diff_list.append({
                    "key": key,
                    "status": "unchanged",
                    "value": dict1[key]
                })
            else:
                diff_list.append({
                    "key": key,
                    "status": "changed",
                    "old_value": dict1[key],
                    "new_value": dict2[key]
                })
        elif key in dict1:
            diff_list.append({
                "key": key,
                "status": "removed",
                "value": dict1[key]
            })
        else:  # key in dict2
            diff_list.append({
                "key": key,
                "status": "added",
                "value": dict2[key]
            })

    return diff_list
