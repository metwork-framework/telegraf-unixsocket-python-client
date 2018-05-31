default: all

all:
	python setup.py build

install: all
	python setup.py install

develop: all
	python setup.py develop

clean:
	find . -type f -name "*.pyc" -delete >/dev/null 2>&1
	find . -type d -name "__pycache__" -exec rm -Rf {} \;
	find . -type d -name "*.egg-info" -exec rm -Rf {} \;
	rm -f MANIFEST
	rm -Rf build
	rm -Rf dist

test:
	flake8 .
	cd tests && nosetests

upload:
	python setup.py sdist register upload

release: test clean upload clean
