author = 'Eden Thiago Ferreira'
import sys
from coletar_dados import *
from time import sleep

repet = int(sys.argv[1])
for i in range(repet):
    print(repet)
    coletar_normal()
    sleep(2)
imprimir_dados()

