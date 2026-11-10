import os
import shutil
from funciones import moverdoc, moverimg, moversoft

os.chdir("/Users/fyeray/Desktop/Descargas") # Buscar la carpeta donde trabajar
print(os.getcwd())
print(os.listdir())

moverdoc()
moverimg()
moversoft()