__author__ = 'Eden Thiago Ferreira'
from math import sqrt

class Ponto:

    def __init__(self,x,y):
        self.__x,self.__y = x, y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value):
        self.__y = value

    def __sub__(self, other):
        """retorna a distancia entre o ponto instanciado ao outro"""
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))