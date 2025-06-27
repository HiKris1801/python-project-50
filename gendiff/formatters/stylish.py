# Constants for readability
INDENT_SIZE = 4
STATUS_INDENT = 2  # Spaces before status symbol
SPACE_AFTER_STATUS = ' '  # Space after status symbol


def get_base_indent(depth):
    """Calculates the base indentation for the current depth level."""
    return ' ' * (depth * INDENT_SIZE)


def get_line_prefix(depth, status_char=' '):
    """
    Generates the prefix for a line, including base indentation,
    status symbol, and space after the symbol.
    """
    base_indent = get_base_indent(depth)
    return (
        f"{base_indent}"
        f"{' ' * STATUS_INDENT}"
        f"{status_char}{SPACE_AFTER_STATUS}"
    )


def stringify(value, depth):
    """
    Converts a value to its string representation.
    Handles dictionaries recursively, and special values (True, False, None).
    """
    if isinstance(value, dict):
        item_indent = get_base_indent(depth + 1) + ' ' * (STATUS_INDENT + 2)
        closing_brace_indent = get_base_indent(depth + 1)

        lines = ['{']
        for k, v in value.items():
            lines.append(f"{item_indent}{k}: {stringify(v, depth + 1)}")
        lines.append(f"{closing_brace_indent}}}")
        return '\n'.join(lines)

    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, str) and not value:
        return ''  # Space for empty values

    return str(value)


def render_node(node, depth):
    """
    Renders a single node of the diff tree into a list of formatted strings.
    """
    key = node['key']
    status = node['status']

    if status == 'nested':
        key_prefix = get_line_prefix(depth, ' ')
        children = format_stylish(node['children'], depth + 1)
        closing_brace_indent = get_base_indent(depth + 1)

        lines = [f"{key_prefix}{key}: {{"]
        lines.extend(children.split('\n')[1:-1])
        lines.append(f"{closing_brace_indent}}}")
        return lines

    elif status == 'unchanged':
        prefix = get_line_prefix(depth, ' ')
        value_str = stringify(node['value'], depth)
        return [f"{prefix}{key}: {value_str}"]

    elif status == 'added':
        prefix = get_line_prefix(depth, '+')
        value_str = stringify(node['value'], depth)
        return [f"{prefix}{key}: {value_str}"]

    elif status == 'removed':
        prefix = get_line_prefix(depth, '-')
        value_str = stringify(node['value'], depth)
        return [f"{prefix}{key}: {value_str}"]

    elif status == 'changed':
        removed_prefix = get_line_prefix(depth, '-')
        added_prefix = get_line_prefix(depth, '+')
        old_value = stringify(node['old_val'], depth)
        new_value = stringify(node['new_val'], depth)
        return [
            f"{removed_prefix}{key}: {old_value}",
            f"{added_prefix}{key}: {new_value}"
        ]
    else:
        raise ValueError(f"Unknown status: {status}")  


def format_stylish(diff_list, depth=0):
    """
    Formats the diff tree into a stylish string output.
    """
    lines = ["{"]

    for node in diff_list:
        lines.extend(render_node(node, depth))

    lines.append("}")

    return '\n'.join(lines)
