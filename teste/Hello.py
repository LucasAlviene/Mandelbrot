from ctypes import *
import os

my_functions = CDLL(os.getcwd()+"/my_functions.o")
print(type(my_functions))
print(my_functions.square(10))
print(my_functions.square(8))