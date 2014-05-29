author = 'Eden Thiago Ferreira'
from collections import defaultdict
from random import *
from math import hypot

class Digrafo:  

    def __init__(self):
        self.pontos = set()
        self.pos_pontos = defaultdict(tuple)
        self.arcos = defaultdict(dict)
        self.num_arestas = 0

    def __len__(self):
        return len(self.pontos)

    def add_ponto(self, pt, x, y):
        self.pontos.add(pt)
        self.pos_pontos[pt] = (x, y)

    def add_arco(self,pt_a,pt_b,peso):
        if pt_a not in self.arcos:
            self.arcos[pt_a] = {}
        self.arcos[pt_a][pt_b] = peso

    def dist(self, pt_a, pt_b):
        return hypot(self.pos_pontos[pt_b][0] - self.pos_pontos[pt_a][0],
                     self.pos_pontos[pt_b][1] - self.pos_pontos[pt_a][1])
    

def gerar_de_dataset(path):
    g = Digrafo()
    with open(path+'.co','r') as arq:
        for e in arq.readlines():
            if e[0] == 'v':
                s = e.strip('v ').split(' ')
                g.add_ponto(int(s[0]),int(s[1]),int(s[2]))
                
    with open(path+'.gr','r') as arq:
        for e in arq.readlines():
            if e[0] == 'a':
                s = e.strip('a ').split(' ')
                g.add_arco(int(s[0]),int(s[1]),int(s[2]))
    return g
   
def gerar_aleatoriamente(grid_x, grid_y, max_x, max_y, distancia_min):
    grafo = Digrafo()
    mult_ident_ponto = 10000000 #Multiplicador para identificacao unica de cada ponto adicionado

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
                
    hor = []
    for i in range(grid_x):
        if i%2 == 0:
            for j in range(grid_y):
                hor.append((i*mult_ident_ponto)+j)
        else:
            for j in reversed(range(grid_y)):
                hor.append((i*mult_ident_ponto)+j)
    
    ver = []
    for j in range(grid_y):
        if j%2 == 0:
            for i in range(grid_x):
                ver.append((i*mult_ident_ponto)+j)
        else:        
            for i in reversed(range(grid_x)):
                ver.append((i*mult_ident_ponto)+j)
    
    for i in range(len(hor)-1):
        grafo.add_arco(hor[i], hor[i+1], gerar_distancia(grafo,hor[i],hor[i+1]))
    
    
    for i in range(len(ver)-1):
        grafo.add_arco(ver[i], ver[i+1], gerar_distancia(grafo,ver[i],ver[i+1]))                
    
    l = list(grafo.pontos)
    for i in range(len(grafo)//50):
        pt_a = l[randrange(len(l))]
        pt_b = l[randrange(len(l))]
        grafo.add_arco(pt_a, pt_b, gerar_distancia(grafo,pt_a,pt_b))

    return grafo

def gerar_distancia(grafo, pt_a, pt_b):
    distancia = 0
    while distancia < grafo.dist(pt_a, pt_b):
        distancia = round(grafo.dist(pt_a, pt_b) * uniform(1.0,1.5))
        if distancia < grafo.dist(pt_a, pt_b):
            distancia += 1
    return distancia
