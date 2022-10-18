## Mandelbrot

Trabalho para a cadeira de **Conceito de Linguagem de Programação** onde foi proposto o uso de duas linguagens de programação **C** e **Python**.
No **Python** é renderizado a interface, no **C** é feito o calculo de Mandelbrot.
Utilizamos o **ctypes** para a comunicação entre as duas linguagens.

## Arquivos
**Mandelbrot.c:** Algoritmo de calculo do Mandelbrot.

**main.py:** Interface do programa.

**Mandelbrot.py:** Configuração da comunicação do **Python** com **C**.

## Compilar e Executar

#### Windows
No windows, o **GCC** só compila em 32 bits, por isso, é necessário instalar a versão do 32 bits do Python e configurar no PATH, escolhendo ou não renomar o programa do Python.exe para Python32.exe.
Se fizer isso, execute o comando:
```$ make windows32```

Se não, execute o comando
```$ make install_python32 compile_windows```
E tente rodar o **main.py** usando o Python 32bits.


#### Linux
No linux é mais fácil e direito, só executar o comando:
```$ make linux```

## Pacotes do python utilizados
math, sdl2

## Fontes
Mandelbrot (Algoritmo): https://github.com/dario-marvin/Mandelbrot

CTypes (Conexão Python-C): https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python 

Pysdl2 (Interface): https://www.youtube.com/watch?v=AQsIU1OUyCE 
