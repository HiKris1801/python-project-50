def format_stylish(diff_list):
    def stringify(value):
        if isinstance(value, bool):
            return "true" if value else "false"
        if value is None:
            return "null"
        return str(value)

    lines = ["{"]

    for record in diff_list:
        key = record["key"]
        status = record["status"]

        if status == "unchanged":
            val = stringify(record["value"])
            lines.append(f"    {key}: {val}")
        elif status == "removed":
            val = stringify(record["value"])
            lines.append(f"  - {key}: {val}")
        elif status == "added":
            val = stringify(record["value"])
            lines.append(f"  + {key}: {val}")
        elif status == "changed":
            old_val = stringify(record["old_value"])
            new_val = stringify(record["new_value"])
            lines.append(f"  - {key}: {old_val}")
            lines.append(f"  + {key}: {new_val}")

    lines.append("}")
    return "\n".join(lines)
