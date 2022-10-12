install_python:
	pip install -r requirements.txt

install_python32:
	python32 -m pip install -r requirements.txt

compile_windows: 
	gcc -shared -o Mandelbrot.o Mandelbrot.c

windows: install_python compile_windows
	python main.py

windows32: install_python32 compile_windows
	python32 main.py

compile_linux: install_python
	cc -fPIC -shared -o Mandelbrot.o Mandelbrot.c

linux: compile_linux
	python3 main.py
