author = 'Eden Thiago Ferreira'
import time
from pqdict import *
from grafos import *

class Dijkstra:
        
    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.pt_a = None
        self.pt_b = None
        self.anterior = {}
        self.dist_total = 0
        self.visitados = set()
        self.nao_visitados = PQDict()
        self.num_passos = 0
        self.__caminho = []
    
    def processar_ponto(self, pt_atual, dist_atual):
        for pt in self.grafo.arcos[pt_atual]:
            if pt not in self.visitados and (pt not in self.nao_visitados or self.nao_visitados[pt] > dist_atual + self.grafo.arcos[pt_atual][pt]):
                self.nao_visitados[pt] = dist_atual + self.grafo.arcos[pt_atual][pt]
                self.anterior[pt] = pt_atual
    
    def executar(self, pt_a, pt_b):
        self.pt_a = pt_a
        self.pt_b = pt_b
        self.nao_visitados[pt_a] = 0
        
        while self.nao_visitados:
            self.num_passos += 1
            pt_atual, dist_atual = self.nao_visitados.popitem()
            self.processar_ponto(pt_atual, dist_atual)            
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
            if pt_atual == pt_b:
                break
    
    @property
    def caminho(self):
        if not self.__caminho:
            self.__caminho = _caminho(self.anterior, self.pt_a, self.pt_b)
        return self.__caminho
        
class AStar:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.pt_a = None
        self.pt_b = None
        self.anterior = {}
        self.dist_total = 0
        self.visitados = set()
        self.nao_visitados = PQDict()
        self.distancia = {}
        self.num_passos = 0
        self.__caminho = []
    
    def heuristica(self,pt):
        #return 0
        return self.grafo.dist(pt, self.pt_b)
    
    def processar_ponto(self, pt_atual, dist_atual):
        for pt in self.grafo.arcos[pt_atual]:
            if pt not in self.visitados and (pt not in self.distancia or self.distancia[pt] > dist_atual + self.grafo.arcos[pt_atual][pt]):
                self.distancia[pt] = dist_atual + self.grafo.arcos[pt_atual][pt]
                self.nao_visitados[pt] = dist_atual + self.grafo.arcos[pt_atual][pt] + self.heuristica(pt)
                self.anterior[pt] = pt_atual
                if pt_atual == 0:
                    print('processar', self.distancia[pt], self.nao_visitados[pt],self.anterior[pt])
    
    def executar(self, pt_a, pt_b):
        self.pt_a = pt_a
        self.pt_b = pt_b
        self.nao_visitados[pt_a] = 0 + self.heuristica(pt_a)
        self.distancia[pt_a] = 0
        
        while self.nao_visitados:
            self.num_passos += 1
            pt_atual = self.nao_visitados.popitem()[0]
            dist_atual = self.distancia[pt_atual]
            if pt_atual == 0:
                print('executar', pt_atual, dist_atual)
            self.processar_ponto(pt_atual, dist_atual)           
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
            if pt_atual == pt_b:
                break
    
    @property
    def caminho(self):
        if not self.__caminho:
            self.__caminho = _caminho(self.anterior, self.pt_a, self.pt_b)
        return self.__caminho
                
                
def _caminho(anterior, pt_a, pt_b):
    caminho = list()
    pt_atual = pt_b
    while pt_atual != pt_a:
        caminho.append(pt_atual)
        if pt_atual == 0:
            print('erroa: ',anterior,'\nerroc: ',caminho)
        pt_atual = anterior[pt_atual]
        
    caminho.append(pt_atual)
    caminho.reverse()
    return caminho
        
