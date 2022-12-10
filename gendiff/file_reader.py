import json
import yaml
from yaml.loader import SafeLoader


def get_data(file):
    with open(file) as data:
        if file[-4:] == 'json':
            return json.load(data)
        elif file[-4:] == '.yml' or file[-4:] == 'yaml':
            return yaml.load(data, Loader=SafeLoader)
