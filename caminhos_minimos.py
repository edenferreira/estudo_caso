author = 'Eden Thiago Ferreira'
from time import *
from pqdict import *
from grafos import *

class Dijkstra:
        
    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.pt_o = None
        self.pt_d = None
        self.anterior = {}
        self.dist_total = 0
        self.visitados = set()
        self.nao_visitados = PQDict()
        self.num_passos = 0
        self.tempo_execucao = 0
        self.__caminho = []

    def processar_ponto(self, pt_atual, dist_atual):
        for pt, dist in self.grafo.arcos[pt_atual]:
            if pt not in self.visitados and (pt not in self.nao_visitados or self.nao_visitados[pt] > dist_atual + dist):
                self.nao_visitados[pt] = dist_atual + dist
                self.anterior[pt] = pt_atual
    
    def __executar(self, pt_o, pt_d):
        self.pt_o = pt_o
        self.pt_d = pt_d
        self.nao_visitados[pt_o] = 0
        
        while self.nao_visitados:
            self.num_passos += 1
            pt_atual, dist_atual = self.nao_visitados.popitem()
            self.processar_ponto(pt_atual, dist_atual)
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
            if pt_atual == pt_d:
                break

    def executar(self, pt_o, pt_d):
        t_ini = time()
        self.__executar(pt_o, pt_d)
        t_fim = time()
        self.tempo_execucao = round(t_fim - t_ini, 3)

    
    @property
    def caminho(self):
        if not self.__caminho:
            self.__caminho = _caminho(self.anterior, self.pt_o, self.pt_d)
        return self.__caminho
        
class AStar:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.pt_o = None
        self.pt_d = None
        self.anterior = {}
        self.dist_total = 0
        self.visitados = set()
        self.nao_visitados = PQDict()
        self.distancia = {}
        self.num_passos = 0
        self.__caminho = []
    
    def heuristica(self,pt):
        return self.grafo.dist(pt, self.pt_d)
    
    def processar_ponto(self, pt_atual, dist_atual):
        for pt, dist in self.grafo.arcos[pt_atual]:
            if pt not in self.visitados and (pt not in self.distancia or self.distancia[pt] > dist_atual + dist):
                self.distancia[pt] = dist_atual + dist
                self.nao_visitados[pt] = dist_atual + dist + self.heuristica(pt)
                self.anterior[pt] = pt_atual
                if pt_atual == 0:
                    print('processar', self.distancia[pt], self.nao_visitados[pt],self.anterior[pt])
    
    def __executar(self, pt_o, pt_d):
        self.pt_o = pt_o
        self.pt_d = pt_d
        self.nao_visitados[pt_o] = 0 + self.heuristica(pt_o)
        self.distancia[pt_o] = 0
        
        while self.nao_visitados:
            self.num_passos += 1
            pt_atual = self.nao_visitados.popitem()[0]
            dist_atual = self.distancia[pt_atual]
            if pt_atual == 0:
                print('__executar', pt_atual, dist_atual)
            self.processar_ponto(pt_atual, dist_atual)           
            self.visitados.add(pt_atual)
            self.dist_total = dist_atual
            if pt_atual == pt_d:
                break

    def executar(self, pt_o, pt_d):
        t_ini = time()
        self.__executar(pt_o, pt_d)
        t_fim = time()
        self.tempo_execucao = round(t_fim - t_ini, 3)
    
    @property
    def caminho(self):
        if not self.__caminho:
            self.__caminho = _caminho(self.anterior, self.pt_o, self.pt_d)
        return self.__caminho
                
                
def _caminho(anterior, pt_o, pt_d):
    caminho = list()
    pt_atual = pt_d
    while pt_atual != pt_o:
        caminho.append(pt_atual)
        if pt_atual == 0:
            print('erroa: ',anterior,'\nerroc: ',caminho)
        pt_atual = anterior[pt_atual]
        
    caminho.append(pt_atual)
    caminho.reverse()
    return caminho
        
