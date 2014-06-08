author = 'Eden Thiago Ferreira'
import sys
from coletar_dados import *
from time import sleep

repet = int(sys.argv[1])
for i in range(repet):
    print(i)
    coletar_normal()
    sleep(1)
    imprimir_dados()
    sleep(1)
    recuperar_dados()

coletar_dataset(100)
imprimir_dados(True)
recuperar_dados(True)
