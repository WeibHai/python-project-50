from gendiff.file_reader import get_data
from gendiff.difference_finder import get_diff
from gendiff.formatter.stylish import get_stylish_view
from gendiff.formatter.plain import get_plain_view
from gendiff.formatter.json import get_json_view


def generate_diff(first_file, second_file, formatter='stylish'):
    if formatter == 'plain':
        return get_plain_view(
            get_diff(get_data(first_file), get_data(second_file)))

    elif formatter == 'json':
        return get_json_view(
            get_diff(get_data(first_file), get_data(second_file)))

    elif formatter == 'stylish':
        return get_stylish_view(
            get_diff(get_data(first_file), get_data(second_file)))
