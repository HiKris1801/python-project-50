
def stringify_plain_value(value):
    '''Преобразует значение в строку для формата plain.

    Args:
        value: Значение, которое нужно преобразовать.

    Returns:
        str: Строковое представление значения.
    '''

    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, (dict, list)):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff_tree, path_parts=None):
    '''Форматирует дерево различий в строку в формате plain.

    Args:
        diff_tree: Дерево различий, полученное из функции build_diff_tree.
        path_parts: Список частей пути для текущего уровня вложенности.

    Returns:
        str: Строка в формате plain, представляющая различия.
    '''
    # 1. Инициализация пути и списка строк
    if path_parts is None:
        path_parts = []

    # Здесь будут собираться все сгенерированные строки для текущего уровня
    lines = []

    # 2. Перебор записей в дереве различий
    for record in diff_tree:
        key = record["key"]          # Получаем ключ текущей записи
        status = record["status"]    # Получаем статус изменения

        # Строим полный путь до текущего ключа.
        current_path = ".".join(path_parts + [key])

        # 3. Обработка записей в зависимости от их статуса
        if status == "unchanged":
            # Неизмененные свойства пропускаются в plain-формате.
            # Функция просто переходит к следующей записи в цикле.
            continue

        elif status == "added":
            # Если свойство добавлено:
            # Преобразуем значение в строку, учитывая [complex value]
            value_str = stringify_plain_value(record["value"])
            # Добавляем строку в список lines.
            lines.append(
                f"Property '{current_path}' was added with value: {value_str}"
            )

        elif status == "removed":
            # Если свойство удалено:
            # Добавляем соответствующую строку.
            lines.append(f"Property '{current_path}' was removed")

        elif status == "changed":
            # Если свойство изменено:
            # Преобразуем старое и новое значения в строки
            # с учетом [complex value]).
            old_value_str = stringify_plain_value(record["old_val"])
            new_value_str = stringify_plain_value(record["new_val"])
            # Добавляем строку об изменении.
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value_str} to {new_value_str}"
            )

        elif status == "nested":
            # Если свойство вложенное :
            # 1. Рекурсивный вызов: Вызываем format_plain для дочерних элементов
            nested_result = format_plain(record["children"], path_parts + [key])

            # 2. Проверка результата рекурсии:
            if nested_result:
                lines.append(nested_result)

        else:

            raise ValueError(f"Неизвестный статус: {status}")

    # 4. Соединение всех строк и возврат результата
    return "\n".join(filter(None, lines))
