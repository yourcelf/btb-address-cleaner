all:
	python setup.py sdist
	twine upload dist/*
