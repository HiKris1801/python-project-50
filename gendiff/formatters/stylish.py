def stringify(value, depth):
    if isinstance(value, dict):
        current_indent_level = depth * 4  # 4 пробела на каждый уровень глубины
        next_indent_level = (depth + 1) * 4
        item_indent = ' ' * next_indent_level
        closing_brace_indent = ' ' * current_indent_level
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
    return str(value)


# Вспомогательная функция для генерации отступа
def get_indent(depth, status_char=' '):
    # Базовый отступ: 4 пробела на каждый уровень глубины
    base_indent = ' ' * (depth * 4)
    # Смещение для символа (+, -, или пробел)
    # 2 пробела для выравнивания + символ + 1 пробел
    # 2 пробела + символ + 1 пробел = 4 символа
    return f"{base_indent}  {status_char} "


def render_node(node, depth):
    key = node['key']
    status = node['status']

    # Отступ для элементов на текущем уровне
    # отступ, который применяется перед символом (+, -, пробел)
    base_indent = ' ' * (depth * 4)

    if status == 'nested':
        # Здесь depth+1 передается в format_stylish, так как вложенный узел
        # сам становится новым "корнем" для форматирования
        # с увеличенной глубиной.
        children_formatted = format_stylish(node['children'], depth + 1)

        # Отступ для ключа вложенного узла и его ОТКРЫВАЮЩЕЙ скобки.
        # Это base_indent + 4 пробела (то есть, без символа)
        key_and_open_brace_indent = f"{base_indent}    "

        # Отступ для ЗАКРЫВАЮЩЕЙ скобки вложенного узла.
        closing_brace_indent = key_and_open_brace_indent

        lines = [f"{key_and_open_brace_indent}{key}: {{"]

        # split('\n')[1:-1] удаляет первую и последнюю строку (скобки '{' и '}')
        # из вложенного форматирования, так как мы их добавляем вручную.
        lines.extend(children_formatted.split('\n')[1:-1])
        lines.append(f"{closing_brace_indent}}}")
        return lines

    elif status == 'unchanged':
        # Отступ для неизмененных узлов (4 пробела)
        # Используем пробел как статус-символ
        unchanged_indent = get_indent(depth, ' ')
        return [f"{unchanged_indent}{key}: {stringify(node['value'], depth)}"]

    elif status == 'added':
        # Отступ для добавленных узлов (+ )
        added_indent = get_indent(depth, '+')
        return [f"{added_indent}{key}: {stringify(node['value'], depth)}"]

    elif status == 'removed':
        # Отступ для удаленных узлов (- )
        removed_indent = get_indent(depth, '-')
        return [f"{removed_indent}{key}: {stringify(node['value'], depth)}"]

    elif status == 'changed':
        # Отступ для удаленного старого значения (- )
        removed_indent = get_indent(depth, '-')
        # Отступ для добавленного нового значения (+ )
        added_indent = get_indent(depth, '+')
        return [
            f"{removed_indent}{key}: {stringify(node['old_val'], depth)}",
            f"{added_indent}{key}: {stringify(node['new_val'], depth)}"
        ]
    else:
        raise ValueError(f"Unknown status: {status}")


def format_stylish(diff_list, depth=0):
    # Отступ для корневых скобок '{' и '}'
    # Для depth=0, это пустая строка.
    # Для глубины > 0, это базовый отступ для текущего уровня.
    root_indent = ' ' * (depth * 4)

    lines = [f"{root_indent}{{"]
    for node in diff_list:
        lines.extend(render_node(node, depth))
    lines.append(f"{root_indent}}}")
    return '\n'.join(lines)

