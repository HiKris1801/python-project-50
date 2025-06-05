__all__ = ['generate_diff']


def generate_diff(dict1, dict2):
    result_diff = []
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result_diff.append({
                    "key": key,
                    "status": "unchanged",
                    "value": dict1[key]
                })
            else:
                result_diff.append({
                    "key": key,
                    "status": "removed",
                    "value": dict1[key]
                })
                result_diff.append({
                    "key": key,
                    "status": "added",
                    "value": dict2[key]
                })
        elif key in dict1:
            result_diff.append({
                "key": key,
                "status": "removed",
                "value": dict1[key]
            })
        else:  # key in dict2
            result_diff.append({
                "key": key,
                "status": "added",
                "value": dict2[key]
            })

    return result_diff




