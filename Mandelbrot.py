from ctypes import *
import os
import matplotlib.pyplot as plt
from enum import Enum

functions = CDLL(os.getcwd()+"/Mandelbrot.o")
functions.mandelbrot_calc.argtypes = [c_double, c_double]
functions.mandelbrot_calc.restype = c_int

functions.mandelbrot.argtypes = [c_int,c_int, c_double]
functions.mandelbrot.restype = POINTER(c_int)

# functions.mandelbrot.restype = POINTER(c_int)
# teste = functions.teste()
# print(teste[1])
# print(teste[0])

class Color(Enum):
    BLACK = (0, 0, 0, 255)          # 0
    RED = (255, 0, 0, 255)          # 1
    L_RED = (255, 100, 100, 255)    # 2
    GREEN = (0, 255, 0, 255)        # 3
    L_GREEN = (100, 255, 100, 255)  # 4
    ORANGE = (255, 165, 0, 255)     # 5
    YELLOW = (255, 255, 0, 255)     # 6
    BLUE = (0, 0, 255, 255)         # 7
    L_BLUE = (100, 100, 255, 255)   # 8
    MAGENTA = (255, 0, 255, 255)    # 9
    L_MAGENTA = (255, 224, 255, 255)# 10
    CYAN = (0, 255, 255, 255)       # 11
    L_CYAN =  (224, 255, 255, 255)  # 12
    GRAY = (200, 200, 200, 255)     # 13
    WHITE = (255,255,255, 255)      # 14

center_x = -1.04082816210546
center_y = 0.346341718848392

def Mandelbrot(width,height,factor):
    pointer = functions.mandelbrot(width,height,factor)
    return pointer

def Mandelbrot2(width,height,factor):
    # x_start = -2.0
    # x_fin = 1.0
    # y_start = -1.0
    # y_fin = 1.0
    x_start = center_x - 1.5 * factor
    x_fin = center_x + 1.5 * factor
    y_start = center_y - factor
    y_fin = center_y + factor


    dx = (x_fin - x_start) / (width - 1)
    dy = (y_fin - y_start) / (height - 1)

    vector = [[(0,0,0,0) for x in range(height)] for y in range(width)]

    for i in range(0,height):
        #txt = ""
        for j in range(0,width):
            x = x_start + j * dx
            y = y_fin - i * dy
            value = functions.mandelbrot_calc(x,y)
            color = Color.L_MAGENTA.value
            if (value == 100): color = Color.BLACK.value
            elif (value > 90): color = Color.RED.value
            elif (value > 70): color = Color.L_RED.value
            elif (value > 50): color = Color.ORANGE.value
            elif (value > 30): color = Color.YELLOW.value
            elif (value > 20): color = Color.L_GREEN.value
            elif (value > 10): color = Color.GREEN.value
            elif (value > 5): color = Color.L_CYAN.value
            elif (value > 4): color = Color.CYAN.value
            elif (value > 3): color = Color.L_BLUE.value
            elif (value > 2): color = Color.BLUE.value
            elif (value > 1): color = Color.MAGENTA.value 

            vector[j][i] = color

    #print(vector)
    return vector

#plt.matshow(vector)
#plt.show()