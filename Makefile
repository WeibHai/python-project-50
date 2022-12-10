install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl

s-json:
	poetry run gendiff 'stylish' './tests/fixtures/file1.json' './tests/fixtures/file2.json'
s-yaml:
	poetry run gendiff 'stylish' './tests/fixtures/file1.yml' './tests/fixtures/file2.yml'
p-json:
	poetry run gendiff 'plain' './tests/fixtures/file1.json' './tests/fixtures/file2.json'
p-yaml:
	poetry run gendiff 'plain' './tests/fixtures/file1.yml' './tests/fixtures/file2.yml'
s-r-json:
	poetry run gendiff 'stylish' './tests/fixtures/r_file1.json' './tests/fixtures/r_file2.json'
s-r-yaml:
	poetry run gendiff 'stylish' './tests/fixtures/r_file1.yml' './tests/fixtures/r_file2.yml'
p-r-json:
	poetry run gendiff 'plain' './tests/fixtures/r_file1.json' './tests/fixtures/r_file2.json'
p-r-yaml:
	poetry run gendiff 'plain' './tests/fixtures/r_file1.yml' './tests/fixtures/r_file2.yml'
j-json:
	poetry run gendiff 'json' './tests/fixtures/file1.json' './tests/fixtures/file2.json'
j-yaml:
	poetry run gendiff 'json' './tests/fixtures/file1.yml' './tests/fixtures/file2.yml'
j-r-json:
	poetry run gendiff 'json' './tests/fixtures/r_file1.json' './tests/fixtures/r_file2.json'
j-r-yaml:
	poetry run gendiff 'json' './tests/fixtures/r_file1.yml' './tests/fixtures/r_file2.yml'
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
test-cov:
	poetry run pytest --cov
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
