all: clean venv install

venv:
				virtualenv py3-venv

install: venv
				. py3-venv/bin/activate; pip install -r requirements.txt
				. py3-venv/bin/activate; pip install -e .

build: install
				. py3-venv/bin/activate; python setup.py sdist
				. py3-venv/bin/activate; python setup.py bdist_wheel

release: build; twine upload -r pypi dist/*

clean:
				rm -rf py3-venv build dist *.egg-info