install: Mandelbrot.o
	pip install -r requirements.txt

install32: Mandelbrot.o
	python32 -m pip install -r requirements.txt

Mandelbrot.o: 
	gcc -shared -o Mandelbrot.o .\Mandelbrot.c

start: install
	python .\main.py

start32: install32
	python32 .\main.py
