import json
import yaml
from yaml.loader import SafeLoader


def get_data(dct):
    if dct['format'] == 'json':
        return json.load(dct['data'])
    if dct['format'] == 'yaml':
        return yaml.load(dct['data'], Loader=SafeLoader)
