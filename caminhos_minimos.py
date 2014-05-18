author = 'Eden Thiago Ferreira'
from heapq import *
from grafos import *

class FilaPrioridade:

    def __init__(self, fila=[]):
        heapify(fila)
        self.fila = fila
        self.busca_entrada = dict()
        self.retirado = '<removido>'

    def insert(self, item, prioridade):
        if item in self.busca_entrada:
            self.delete(item)
        entrada = [prioridade, str(item)]
        self.busca_entrada[item] = entrada
        heappush(self.fila, entrada)

    def delete(self, item):
        entrada = self.busca_entrada.pop(item,[float('inf'),'0'])
        entrada[-1] = self.retirado
        return entrada[0]

    def pop(self):
        while self.fila:
            prioridade, item = heappop(self.fila)
            if item is not self.retirado:
                del self.busca_entrada[int(item)]
                return prioridade, int(item)
        raise KeyError('fila vazia')


class Dijkstra:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.num_passos = 0
        self.origem_destino = None
        self.caminho = list()
        self.dist_total = 0
        self.nao_visitados = set(self.grafo.pontos)
        self.visitados = set()
        self.fronteira = FilaPrioridade()

    def processar_pt(self, pt_atual, dist_atual):
        self.visitados.add(pt_atual)
        self.nao_visitados.remove(pt_atual)
        for pt, dist in self.grafo.arcos[pt_atual]:
            if pt not in self.visitados:
                velha_dist = self.fronteira.delete(pt)
                nova_dist = min(velha_dist, dist_atual + dist)
                self.fronteira.insert(pt, nova_dist)

    def executar(self, pt_a, pt_b):
        self.origem_destino = (pt_a, pt_b)
        self.fronteira.insert(pt_a)
        pt_atual = None
        while pt_atual != pt_b and self.nao_visitados:
            dist_atual, pt_atual = self.fronteira.pop()
            self.num_passos += 1
            self.caminho.append(pt_atual)
            self.dist_total = dist_atual
            self.processar_pt(pt_atual, dist_atual)
