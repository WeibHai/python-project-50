#  function returns an intermediate representation of the file difference


def get_diff(first_data, second_data):
    tree_collection = []
    for key in sorted(first_data.keys() | second_data.keys()):
        first = first_data.get(key)
        second = second_data.get(key)

        if isinstance(first, dict) and isinstance(second, dict):
            tree_collection.append({'type': 'parent_dir',
                                    'name': key,
                                    'value': None,
                                    'children': get_diff(first, second)})

        elif first == second:
            tree_collection.append({'type': 'unchanged',
                                    'name': key,
                                    'value': first})

        elif key in first_data and key not in second_data:
            tree_collection.append({'type': 'removed',
                                    'name': key,
                                    'value': first})

        elif key in second_data and key not in first_data:
            tree_collection.append({'type': 'added',
                                    'name': key,
                                    'value': second})

        else:
            tree_collection.append({'type': 'changed',
                                    'name': key,
                                    'value': first,
                                    'value2': second})

    return tree_collection
