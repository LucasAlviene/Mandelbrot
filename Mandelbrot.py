from ctypes import *
import os
from enum import Enum

functions = CDLL(os.getcwd()+"/Mandelbrot.o")

functions.mandelbrot.argtypes = [c_int,c_int, c_double]
functions.mandelbrot.restype = POINTER(c_int)

def Mandelbrot(width,height,factor):
    pointer = functions.mandelbrot(width,height,factor)
    return pointer