install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
test-cov:
	poetry run pytest --cov
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
s-r:
	poetry run gendiff -f 'plain' '/home/mark/work/python-project-50/tests/fixtures/r_file1.json' '/home/mark/work/python-project-50/tests/fixtures/r_file2.yml'
s:
	poetry run gendiff -f 'plain' '/home/mark/work/python-project-50/tests/fixtures/file1.json' '/home/mark/work/python-project-50/tests/fixtures/file2.yml'
