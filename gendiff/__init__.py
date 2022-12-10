from gendiff.file_reader import get_data
from gendiff.difference_finder import get_diff
from gendiff.formatter.stylish import get_stylish_view
from gendiff.formatter.plain import get_plain_view
from gendiff.formatter.json import write_in_json

import json
import yaml
from yaml.loader import SafeLoader