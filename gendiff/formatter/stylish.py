SPACE = ' '
INDENT_MULTIPLIER = 4


def stylish_node(node, depth):
    opener = SPACE * (INDENT_MULTIPLIER * depth - 2)
    closer = SPACE * (INDENT_MULTIPLIER * (depth - 1))

    if isinstance(node, dict):
        result = ["{"]

        for name, value in node.items():
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol=' ',
                name=name, value=stylish_node(value, depth + 1)))
        result.append('{indent}{symbol}'.format(indent=closer, symbol='}'))
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
        children = node.get('children')

        if type == 'added':
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol='+', name=name, value=value))

        elif type == 'removed':
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol='-', name=name, value=value))

        elif type == 'unchanged':
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol=' ', name=name, value=value))

        elif type == 'parent_dir':
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol=' ',
                name=name, value=stylish(children, depth + 1)))

        else:
            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol='-', name=name, value=value))

            result.append('{indent}{symbol} {name}: {value}'.format(
                indent=opener, symbol='+',
                name=name, value=stylish_node(node.get('value2'), depth + 1)))

    result.append('{indent}{symbol}'.format(indent=closer, symbol='}'))

    return '\n'.join(result)


def get_stylish_view(tree):
    result = stylish(tree, depth=1)

    replace_values = (("False", "false"), ("True", "true"), ("None", "null"))

    for first_value, second_value in replace_values:
        result = result.replace(first_value, second_value)

    return result
