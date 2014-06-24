author = 'Eden Thiago Ferreira'
import sys
from coletar_dados import *
from time import sleep

repet = int(sys.argv[1])

for i in range(repet):
    print(i)
    coletar_normal()
    imprimir_dados()
    recuperar_dados()

repet = int(sys.argv[2])

coletar_dataset(repet)
imprimir_dados(True)
recuperar_dados(True)
