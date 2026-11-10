import os
import shutil
from variables import doc_types, img_types, software_types

def moverdoc():
    if not os.path.exists("./Documentos"):
        os.mkdir('Documentos')
    for i in os.listdir():
        if i.endswith(doc_types):
            shutil.move(i, r"./Documentos")

def moverimg():
    if not os.path.exists("./Imágenes"):
        os.mkdir('Imágenes')
    for i in os.listdir():
        if i.endswith(img_types):
            shutil.move(i, r"./Imágenes")

def moversoft():
    if not os.path.exists("./Software"):
        os.mkdir('Software')
    for i in os.listdir():
        if i.endswith(software_types):
            shutil.move(i, r"./Software")