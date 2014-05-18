__author__ = 'Eden Thiago Ferreira'
from collections import defaultdict
from plano_cartesiano import *

class _Vertice:

    def __init__(self,cod,dado):
        self.__cod = cod
        self.__dado = dado

    @property
    def cod(self):
        return self.__cod

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self,value):
        self.__dado = value



class _Arco:

    def __init__(self,ver_a,ver_b,peso):
        self.__ver_a,self.__ver_b = ver_a,ver_b
        self.__peso = peso

    @property
    def ver_a(self):
        return self.__ver_a

    @property
    def ver_b(self):
        return self.__ver_b

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self,value):
        self.__peso = value

class Digrafo:

    def __init__(self):
        self.__vertices = set()
        self.__arcos    = defaultdict(list)

    @property
    def vertices(self):
        return self.__vertices

    @property
    def arcos(self):
        return self.__arcos

    def add_vertice(self,dado):
        ver = _Vertice(len(self.__vertices),dado)
        self.__vertices.add(ver)

    def add_arco(self,ver_a,ver_b,peso):
        arc = _Arco(ver_a,ver_b,peso)
        self.__arcos[ver_a].append(arc)