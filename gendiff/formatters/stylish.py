def format_stylish(diff_list, depth=0):
    def stringify(value, depth):
        if isinstance(value, dict):
            indent = ' ' * ((depth + 1) * 4)
            closing_indent = ' ' * (depth * 4)
            lines = ['{']
            for k, v in value.items():
                lines.append(f"{indent}{k}: {stringify(v, depth + 1)}")
            lines.append(f"{closing_indent}}}")
            return '\n'.join(lines)
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        if value is None:
            return 'null'
        return str(value)

    lines = []
    indent_size = depth * 4
    base_indent = ' ' * indent_size
    add_indent = base_indent + '  + '
    rem_indent = base_indent + '  - '
    plain_indent = base_indent + '    '

    lines.append(f"{base_indent}{{")

    for node in diff_list:
        key = node['key']
        status = node['status']

        if status == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{plain_indent}{key}: {{")
            lines.extend(children.split('\n')[1:-1])
            lines.append(f"{plain_indent}}}")

        elif status == 'unchanged':
            value = stringify(node['value'], depth)
            lines.append(f"{plain_indent}{key}: {value}")

        elif status == 'added':
            value = node['value']
            if isinstance(value, dict):
                stringified = stringify(value, depth + 1)
                indented = '\n'.join(stringified.split('\n'))
                lines.append(f"{add_indent}{key}: {indented}")
            else:
                lines.append(f"{add_indent}{key}: {stringify(value, depth)}")

        elif status == 'removed':
            value = node['value']
            if isinstance(value, dict):
                stringified = stringify(value, depth + 1)
                indented = '\n'.join(stringified.split('\n'))
                lines.append(f"{rem_indent}{key}: {indented}")
            else:
                lines.append(f"{rem_indent}{key}: {stringify(value, depth)}")

        elif status == 'changed':
            old = node['old_val']
            new = node['new_val']
            if isinstance(old, dict):
                stringified_old = stringify(old, depth + 1)
                old_lines = '\n'.join(stringified_old.split('\n'))
                lines.append(f"{rem_indent}{key}: {old_lines}")
            else:
                lines.append(f"{rem_indent}{key}: {stringify(old, depth)}")

            if isinstance(new, dict):
                stringified_new = stringify(new, depth + 1)
                new_lines = '\n'.join(stringified_new.split('\n'))
                lines.append(f"{add_indent}{key}: {new_lines}")
            else:
                lines.append(f"{add_indent}{key}: {stringify(new, depth)}")

        else:
            raise ValueError(f"Unknown status: {status}")

    lines.append(f"{base_indent}}}")
    return '\n'.join(lines)
