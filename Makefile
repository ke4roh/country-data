.PHONY: setup-dev check-schema check-commits validate-all

# Set up the Python environment and install dependencies
setup-dev:
	@echo "🔧 Setting up development environment with Poetry..."
	@which poetry > /dev/null || (echo "❌ Poetry is not installed. Install it from https://python-poetry.org/" && exit 1)
	poetry install --no-root
	poetry run pre-commit install
	@echo "✅ Poetry environment ready."
	@echo "ℹ️  Run \`cz check\` to validate commit messages manually."

# Validate all JSON files against schema
check-schema:
	poetry run python tools/validate_all.py

# Validate commits
check-commits:
	poetry run cz check --rev-range origin/main...HEAD

check-all: check-schema check-commits

