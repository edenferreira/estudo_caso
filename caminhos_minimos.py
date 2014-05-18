author = 'Eden Thiago Ferreira'
from heapq import *
from grafos import *

class FilaPrioridade:

    def __init__(self, fila=[]):
        heapify(fila)
        self.fila = fila
        self.busca_entrada = dict({i[-1]: i for i in self.fila})
        self.retirado = '<retirado>'

    def insert(self, item, prioridade=0):
        if item in self.busca_entrada:
            self.delete(item)
        entrada = [prioridade, item]
        self.busca_entrada[item] = entrada
        heappush(self.fila, entrada)

    def delete(self, item):
        entrada = self.busca_entrada.pop(item)
        entrada[-1] = self.retirado
        return entrada[0]

    def pop(self):
        while self.fila:
            prioridade, item = heappop(self.fila)
            if item is not self.retirado:
                del self.busca_entrada[item]
                return prioridade, item
        raise KeyError('fila vazia')


class Dijkstra:

    def __init__(self, grafo=Digrafo()):
        self.grafo = grafo
        self.num_passos = 0
        self.origem_destino = None
        self.caminho = list()
        self.dist_total = 0
        self.nao_visitados = set(self.grafo.vertices)
        self.visitados = set()
        self.fronteira = FilaPrioridade()
        self.anterior = defaultdict((None, float('inf')))

    def processar_pt(self, pt_atual, dist_atual):
        self.visitados.add(pt_atual)
        self.nao_visitados.remove(pt_atual)
        for arc in self.grafo.arcos[pt_atual]:
            if arc.ver_b not in self.visitados:
                velha_dist = self.fronteira.delete(arc.ver_b)
                nova_dist = min(velha_dist, dist_atual + arc.peso)
                self.fronteira.insert(arc.ver_b, nova_dist)

    def executar(self, ver_a, ver_b):
        self.origem_destino = (ver_a, ver_b)
        self.fronteira.insert(ver_a)
        pt_atual = None
        while pt_atual != ver_b and self.nao_visitados:
            dist_atual, pt_atual = self.fronteira.pop()
            self.num_passos += 1
            self.caminho.append(pt_atual)
            self.dist_total = dist_atual
            self.processar_pt(pt_atual, dist_atual)