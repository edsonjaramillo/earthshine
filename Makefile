build:
	@uv run build.py

format:
	@uv run ruff format

lint:
	@uv run ruff check
