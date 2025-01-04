build:
	@uv run build.py

contrast:
	@uv run contrast.py

format:
	@uv run ruff format

lint:
	@uv run ruff check
