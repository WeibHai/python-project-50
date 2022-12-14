from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("path, path2, formatter, expected", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', 'stylish', 'tests/fixtures/res_stylish.txt'),
    ('tests/fixtures/r_file1.yml', 'tests/fixtures/r_file2.json', 'stylish', 'tests/fixtures/res_rec_stylish.txt'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', 'plain', 'tests/fixtures/res_plain.txt'),
    ('tests/fixtures/r_file1.yml', 'tests/fixtures/r_file2.json', 'plain', 'tests/fixtures/res_rec_plain.txt'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', 'json', 'tests/fixtures/inter_represent.txt'),
    ('tests/fixtures/r_file1.yml', 'tests/fixtures/r_file2.json', 'json', 'tests/fixtures/inter_represent_r.txt')])
def test_generate_diff(path, path2, formatter, expected):
    with open(expected, 'r') as file:
        result = file.read()
    assert generate_diff(path, path2, formatter) == result
