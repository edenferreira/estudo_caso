author = 'Eden Thiago Ferreira'
from math import sqrt

class Ponto:

    def __init__(self,x,y):
        self.x,self.y = x, y

    def sub(self, other):
        """retorna a distancia entre o ponto instanciado ao outro"""
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))