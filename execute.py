author = 'Eden Thiago Ferreira'
import sys
from coletar_dados import *
from time import sleep

#repet = int(sys.argv[1])
repet = 1
for i in range(repet):
    print(i)
    coletar_normal()
    sleep(1)
    imprimir_dados()
    sleep(1)
    recuperar_dados()

