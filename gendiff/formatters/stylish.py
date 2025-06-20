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


def render_simple_line(key, value, indent):
    return f"{indent}{key}: {value}"


def render_changed(key, old, new, depth):
    indent = ' ' * (depth * 4)
    rem_indent = indent + '  - '
    add_indent = indent + '  + '
    return [
        f"{rem_indent}{key}: {stringify(old, depth)}",
        f"{add_indent}{key}: {stringify(new, depth)}"
    ]


def render_node(node, depth):
    key = node['key']
    status = node['status']
    indent = ' ' * (depth * 4)
    plain_indent = indent + '    '
    rem_indent = indent + '  - '
    add_indent = indent + '  + '

    if status == 'nested':
        children = format_stylish(node['children'], depth + 1)
        lines = (
            [f"{plain_indent}{key}: {{"]
            + children.split('\n')[1:-1]
            + [f"{plain_indent}}}"]
        )
        return lines
    elif status == 'unchanged':
        return [
            render_simple_line(
                key,
                stringify(node['value'], depth),
                plain_indent
            )
        ]
    elif status == 'added':
        return [f"{add_indent}{key}: {stringify(node['value'], depth)}"]
    elif status == 'removed':
        return [f"{rem_indent}{key}: {stringify(node['value'], depth)}"]
    elif status == 'changed':
        return render_changed(key, node['old_val'], node['new_val'], depth)
    else:
        raise ValueError(f"Unknown status: {status}")


def format_stylish(diff_list, depth=0):
    indent = ' ' * (depth * 4)
    lines = [f"{indent}{{"]
    for node in diff_list:
        lines.extend(render_node(node, depth))
    lines.append(f"{indent}}}")
    return '\n'.join(lines)
