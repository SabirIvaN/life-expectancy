run:
	./src/app.py

build:
	chmod +x ./src/app.py

start:
	chmod +x ./src/app.py
	./src/app.py

upgrade:
	python3 -m pip install --upgrade pip

install:
	python3 -m pip install matplotlib
	python3 -m pip install seaborn
	python3 -m pip install pandas
