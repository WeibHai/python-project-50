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
            value = plain_value(node.get('value'))

            if type_node == 'parent_dir':
                children = node.get('children')

                return list(map(lambda element: inner(
                    element, path + [name]), children))

            elif type_node == 'added':
                path.append(name)
                path = '.'.join(path)

                return f"Property '{path}' was added with value: {value}"

            elif type_node == 'removed':
                path.append(name)
                path = '.'.join(path)

                return f"Property '{path}' was removed"

            elif type_node == 'changed':
                value2 = plain_value(node.get('value2'))
                path.append(name)
                path = '.'.join(path)

                return (
                    f"Property '{path}' was updated. From {value} to {value2}")

        return '\n'.join(flatten(result))

    return inner(tree, path=[])


def get_plain_view(tree):
    result = plain(tree)

    replace_values = (("False", "false"), ("True", "true"), ("None", "null"))

    for first_value, second_value in replace_values:
        result = result.replace(first_value, second_value)

    return result
