from gendiff.file_reader import get_data
from gendiff.difference_finder import get_diff
from gendiff import generate_diff
from tests.fixtures import expected_results


def test_file_reader():
    assert get_data('tests/fixtures/file1.json') == expected_results.data_file1
    assert get_data('tests/fixtures/file2.yml') == expected_results.data_file2
    assert get_data('tests/fixtures/r_file1.json') == expected_results.data_r_file1
    assert get_data('tests/fixtures/r_file2.yml') == expected_results.data_r_file2


def test_difference_finder():
    assert get_diff(get_data('tests/fixtures/file1.json'), get_data('tests/fixtures/file2.json')) == expected_results.internal_representation
    assert get_diff(get_data('tests/fixtures/file1.yml'), get_data('tests/fixtures/file2.yml')) == expected_results.internal_representation
    assert get_diff(get_data('tests/fixtures/r_file1.json'), get_data('tests/fixtures/r_file2.json')) == expected_results.r_internal_representation
    assert get_diff(get_data('tests/fixtures/r_file1.yml'), get_data('tests/fixtures/r_file2.yml')) == expected_results.r_internal_representation


def test_engine():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', formatter='stylish') == expected_results.result_stylish
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', formatter='stylish') == expected_results.result_stylish
    assert generate_diff('tests/fixtures/r_file1.json', 'tests/fixtures/r_file2.json', formatter='stylish') == expected_results.result_stylish_r
    assert generate_diff('tests/fixtures/r_file1.yml', 'tests/fixtures/r_file2.yml', formatter='stylish') == expected_results.result_stylish_r

    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', formatter='plain') == expected_results.result_plain
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', formatter='plain') == expected_results.result_plain
    assert generate_diff('tests/fixtures/r_file1.json', 'tests/fixtures/r_file2.json', formatter='plain') == expected_results.result_plain_r
    assert generate_diff('tests/fixtures/r_file1.yml', 'tests/fixtures/r_file2.yml', formatter='plain') == expected_results.result_plain_r
