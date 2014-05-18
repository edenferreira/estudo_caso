author = 'Eden Thiago Ferreira'
from collections import defaultdict
from random import *
from math import sqrt

class Digrafo:

    def __init__(self):
        self.pontos = set()
        self.pos_pontos = defaultdict(tuple)
        self.arcos = defaultdict(list)
        self.num_arestas = 0

    def __len__(self):
        return len(self.pontos)

    def add_ponto(self, pt, x, y):
        self.pontos.add(pt)
        self.pos_pontos[pt] = (x, y)

    def add_arco(self,pt_a,pt_b,peso):
        self.arcos[pt_a].append((pt_b, peso))

    def dist(self, pt_a, pt_b):
        return sqrt(((self.pos_pontos[pt_b][0] - self.pos_pontos[pt_a][0]) ** 2)
                    + ((self.pos_pontos[pt_b][1] - self.pos_pontos[pt_a][1]) ** 2))

    @staticmethod
    def gerar_aleatoriamente(grid_x, grid_y, max_x, max_y, distancia_min):
        grafo = Digrafo()
        mult_ident_ponto = 10000000 #Multiplicador para identificação unica de cada ponto adicionado

        fracao_x, fracao_y = max_x/grid_x, max_y/grid_y
        tam_min_x = distancia_min / 2
        tam_max_x = fracao_x - tam_min_x
        tam_min_y = distancia_min / 2
        tam_max_y = fracao_y - tam_min_y

        x_1, x_2 = tam_min_x, tam_max_x
        y_1, y_2 = tam_min_y, tam_max_y
        p_x = p_y = {}

        for i in range(grid_x):
            p_x[i] = (x_1, x_2)
            x_1 += fracao_x
            x_2 += fracao_x
        for i in range(grid_y):
            p_y[i] = (y_1, y_2)
            y_1 += fracao_y
            y_2 += fracao_y

        for key_x, x in p_x.items():
            for key_y, y in p_y.items():
                grafo.add_ponto((key_x * mult_ident_ponto) + key_y, uniform(x[0], x[1]), uniform(y[0], y[1]))

        for i in range(grid_x - 1):
            for j in range(grid_y - 1):
                pt_atual = (i * mult_ident_ponto) + j
                pt_direita = (i * mult_ident_ponto) + j + 1
                pt_abaixo = ((i + 1) * mult_ident_ponto) + j
                if (i / mult_ident_ponto) % 2 == 0:
                    grafo.add_arco(pt_atual, pt_direita, grafo.dist(pt_atual,pt_direita) * uniform(1,1.5))
                else:
                    grafo.add_arco(pt_direita, pt_atual, grafo.dist(pt_direita, pt_atual) * uniform(1,1.5))
                if j % 2 == 0:
                    grafo.add_arco(pt_abaixo, pt_atual, grafo.dist(pt_abaixo, pt_atual) * uniform(1,1.5))
                else:
                    grafo.add_arco(pt_atual, pt_abaixo, grafo.dist(pt_atual, pt_abaixo) * uniform(1,1.5))

        for i in range(len(grafo)//10):
            pt_a, pt_b = sample(grafo.pontos,2)
            grafo.add_arco(pt_a, pt_b, grafo.dist(pt_a, pt_b) * uniform(1,1.5))

        return grafo