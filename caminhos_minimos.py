author = 'Eden Thiago Ferreira'
import time
from grafos import *   
from pqdict import *

class Dijkstra:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.num_passos = 0
        self.origem_destino = None
        self.anterior = {}
        self.dist_total = 0
        self.nao_visitados = PQDict()
        self.visitados = set()
        self.distancia = {}
    
    def processa_arco(self, pt_atual, dist_atual, pt, dist):
        if pt not in self.visitados and self.distancia.setdefault(pt, float('inf')) > dist_atual + dist:
            self.nao_visitados[pt] = dist_atual + dist
            self.distancia[pt] = dist_atual + dist
            self.anterior[pt] = pt_atual        
    
    def executar(self, pt_a, pt_b):        
        self.num_passos = 0
        self.origem_destino = (pt_a, pt_b)
        self.nao_visitados[pt_a] = 0
        self.distancia[pt_a] = 0
        pt_atual = None
        while pt_atual != pt_b and self.nao_visitados:
            self.num_passos += 1
            pt_atual = self.nao_visitados.popitem()[0]
            dist_atual = self.distancia[pt_atual]
            for pt, dist in self.grafo.arcos[pt_atual]:
                self.processa_arco(pt_atual, dist_atual, pt, dist)
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
        print(self.distancia[pt_atual])
    
    @property
    def caminho(self):
        caminho = list()
        pt_atual = self.origem_destino[1]
        while pt_atual != self.origem_destino[0]:
            caminho.append(pt_atual)
            pt_atual = self.anterior[pt_atual]
        caminho.append(pt_atual)
        caminho.reverse()
        return caminho
        
class AStar:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.num_passos = 0
        self.origem_destino = None
        self.anterior = {}
        self.dist_total = 0
        self.nao_visitados = PQDict()
        self.visitados = set()
        self.distancia = {}
    
    def processa_arco(self, pt_atual, dist_atual, pt, dist):
        if pt not in self.visitados and self.distancia.setdefault(pt, float('inf')) > dist_atual + dist:
            self.nao_visitados[pt] = dist_atual + dist + self.grafo.dist(pt_atual,self.origem_destino[1])
            self.distancia[pt] = dist_atual + dist
            self.anterior[pt] = pt_atual
    
    def executar(self, pt_a, pt_b):        
        self.num_passos = 0
        self.origem_destino = (pt_a, pt_b)
        self.nao_visitados[pt_a] = 0
        self.distancia[pt_a] = 0
        pt_atual = None
        while pt_atual != pt_b and self.nao_visitados:
            self.num_passos += 1
            pt_atual = self.nao_visitados.popitem()[0]
            dist_atual = self.distancia[pt_atual]
            for pt, dist in self.grafo.arcos[pt_atual]:
                self.processa_arco(pt_atual, dist_atual, pt, dist)
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
        print(self.distancia[pt_atual])
    
    @property
    def caminho(self):
        caminho = list()
        pt_atual = self.origem_destino[1]
        while pt_atual != self.origem_destino[0]:
            caminho.append(pt_atual)
            pt_atual = self.anterior[pt_atual]
        caminho.append(pt_atual)
        caminho.reverse()
        return caminho
