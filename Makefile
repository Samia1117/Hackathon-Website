install:
	pip install --upgrade pip setuptools wheel &&\
		pip install -r requirements.txt

format:
	black *.py
	
lint:
	pylint --disable=R,C *.py
		