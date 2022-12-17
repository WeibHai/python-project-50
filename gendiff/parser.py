import json
import yaml
from yaml.loader import SafeLoader


#  the function parse the data that is passed to it from the file


def get_data(dct):
    if dct['format'] == 'json':
        return json.load(dct['data'])
    if dct['format'] == 'yaml':
        return yaml.load(dct['data'], Loader=SafeLoader)
