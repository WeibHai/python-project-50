def flatten(tree):
    result = []

    def inner(subtree):
        for item in subtree:
            if isinstance(item, list):
                inner(item)

            elif len(item) > 0:
                result.append(item)
    inner(tree)
    return result


def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, str):
        return f"'{value}'"

    else:
        return value


def plain(tree):
    result = []

    def inner(node, path):
        if isinstance(node, list):
            for element in node:
                result.append(plain(element))

        elif isinstance(node, dict):
            name = node.get('name')
            type_node = node.get('type')
            children = node.get('children')
            value = node.get('value')
            value2 = node.get('value2')

            if type_node == 'parent_dir':
                return list(map(lambda element: inner(
                    element, path + [name]), children))

            elif type_node == 'added':
                path.append(name)
                return "Property '{path}' was added with value: {value}".format(
                    path='.'.join(path), value=plain_value(value))

            elif type_node == 'removed':
                path.append(name)
                return "Property '{path}' was removed".format(
                    path='.'.join(path))

            elif type_node == 'changed':
                path.append(name)
                return ("Property '{}' was updated. From {} to {}".format(
                    '.'.join(path), plain_value(value), plain_value(value2)))

        return '\n'.join(flatten(result))

    return inner(tree, path=[])


def get_plain_view(tree):
    result = plain(tree)

    replace_values = (("False", "false"), ("True", "true"), ("None", "null"))

    for first_value, second_value in replace_values:
        result = result.replace(first_value, second_value)

    return result
