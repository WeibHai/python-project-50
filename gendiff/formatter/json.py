import json


def preparation_node(node):
    if isinstance(node, dict):
        result = []

        for name, value in node.items():
            result.append({f'{name}': preparation_node(value)})

        return result
    else:
        return node


def preparation_tree(tree):
    result = []

    for node in tree:
        name = node.get('name')
        type = node.get('type')
        raw_value = node.get('value')
        value = preparation_node(node.get('value'))
        value2 = preparation_node(node.get('value2'))

        if type == 'added':
            result.append({f'+ {name}': value})

        elif type == 'removed':
            result.append({f'- {name}': value})

        elif type == 'unchanged':
            result.append({f'{name}': value})

        elif type == 'root':
            result.append({f'{name}': preparation_tree(raw_value)})

        else:
            result.append({f'{name}': {'-': value, '+': value2}})

    return json.dumps(result)


def write_in_json(tree):
    with open("result_diff.json", "w") as my_file:
        my_file.write(preparation_tree(tree))
