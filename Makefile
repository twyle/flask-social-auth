update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev: requirements-dev.txt
	@pip install -r requirements-dev.txt

run:
	@python main.py

test:
	@python -m pytest
