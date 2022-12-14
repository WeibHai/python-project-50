SPACE = ' '
INDENT_MULTIPLIER = 4
SYMBOL_CLOSE = '}'


def stylish_node(node, depth):
    opener = SPACE * (INDENT_MULTIPLIER * depth - 2)
    closer = SPACE * (INDENT_MULTIPLIER * (depth - 1))

    if isinstance(node, dict):
        result = ["{"]

        for name, value in node.items():
            result.append(f'{opener}  {name}: {stylish_node(value, depth + 1)}')

        result.append(f'{closer}{SYMBOL_CLOSE}')
        return '\n'.join(result)
    else:
        return node


def stylish(tree, depth):
    result = ['{']

    opener = SPACE * (INDENT_MULTIPLIER * depth - 2)
    closer = SPACE * (INDENT_MULTIPLIER * (depth - 1))

    for node in tree:
        name = node.get('name')
        type = node.get('type')
        value = stylish_node(node.get('value'), depth + 1)

        if type == 'added':
            result.append(f'{opener}+ {name}: {value}')

        elif type == 'removed':
            result.append(f'{opener}- {name}: {value}')

        elif type == 'unchanged':
            result.append(f'{opener}  {name}: {value}')

        elif type == 'parent_dir':
            children = stylish(node.get('children'), depth + 1)

            result.append(f'{opener}  {name}: {children}')

        else:
            value2 = stylish_node(node.get('value2'), depth + 1)

            result.append(f'{opener}- {name}: {value}')
            result.append(f'{opener}+ {name}: {value2}')

    result.append(f'{closer}{SYMBOL_CLOSE}')

    return '\n'.join(result)


def get_stylish_view(tree):
    result = stylish(tree, depth=1)

    replace_values = (("False", "false"), ("True", "true"), ("None", "null"))

    for first_value, second_value in replace_values:
        result = result.replace(first_value, second_value)

    return result
