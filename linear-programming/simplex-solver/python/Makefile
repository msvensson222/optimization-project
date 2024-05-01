.PHONY: all install-poetry check-gcloud-auth install-dependencies install-precommit success docs

setup: install-poetry install-dependencies install-precommit success

install-poetry:
	@echo "Installing Poetry..."
	@python3 -m pip show poetry || python3 -m pip install poetry

install-dependencies:
	@echo "Installing dependencies with Poetry..."
	@poetry config virtualenvs.in-project true
	@poetry install

install-precommit:
	@echo "Installing pre-commit hooks..."
	poetry run pre-commit install

success:
	@echo "Success"