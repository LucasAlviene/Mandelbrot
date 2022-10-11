from ctypes import *
import os
from enum import Enum

functions = CDLL(os.getcwd()+"/Mandelbrot.o")

functions.mandelbrot.argtypes = [c_int,c_int, c_double]
functions.mandelbrot.restype = POINTER(c_int)

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