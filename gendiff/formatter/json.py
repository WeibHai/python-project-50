import json


def get_json_view(tree):
    return json.dumps(tree, indent=4)
