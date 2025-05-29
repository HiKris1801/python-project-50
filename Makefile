install:#install dependencies
	uv sync
gendiff:
	uv run gendiff
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check gendiff
test:
	uv run pytest
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
rebuild: lock install build package-install

