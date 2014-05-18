author = 'Eden Thiago Ferreira'
from collections import defaultdict

class _Vertice:

    def __init__(self,cod,dado):
        self.cod = cod
        self.dado = dado

class _Arco:

    def __init__(self,ver_a,ver_b,peso):
        self.ver_a,self.ver_b = ver_a,ver_b
        self.peso = peso

class Digrafo:

    def __init__(self):
        self.vertices = set()
        self.arcos    = defaultdict(list)

    def len(self):
        return len(self.vertices)

    def add_vertice(self,dado):
        ver = _Vertice(len(self.vertices),dado)
        self.vertices.add(ver)

    def add_arco(self,ver_a,ver_b,peso):
        arc = _Arco(ver_a,ver_b,peso)
        self.arcos[ver_a].append(arc)