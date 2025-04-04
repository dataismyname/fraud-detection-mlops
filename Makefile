VENV := .venv

.PHONY: venv install serve clean

venv:
	python -m venv $(VENV)
	. $(VENV)/bin/activate

install:
	pip install -r requirements.txt

serve:
	uvicorn src.inference.app:app --reload

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
