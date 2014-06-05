author = 'Eden Thiago Ferreira'
from random import *
from collections import defaultdict
import math


_mult_ident_ponto = 10000000 #Multiplicador para identificacao unica de cada ponto adicionado

class Digrafo:

    def __init__(self,ident=None):
        self.ident = ident
        self.pontos = set()
        self.pos_pontos = defaultdict(tuple)
        self.arcos = defaultdict(list)
        self.num_arestas = 0

    def __len__(self):
        return len(self.pontos)

    def add_ponto(self, pt, lat, lon):
        self.pontos.add(pt)
        self.pos_pontos[pt] = (lat, lon) #latitude e longitude

    def add_arco(self,pt_a,pt_b,peso):
        self.num_arestas += 1
        self.arcos[pt_a].append((pt_b, peso))

    def dist(self, pt_a, pt_b):
        return self.__dist(self.pos_pontos[pt_a], self.pos_pontos[pt_b])
        #return math.hypot(self.pos_pontos[pt_b][0] - self.pos_pontos[pt_a][0], self.pos_pontos[pt_b][1] - self.pos_pontos[pt_a][1])
    
    def __dist(self, pt_a, pt_b):
        lat1, lon1 = pt_a
        lat2, lon2 = pt_b
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) \
                                                  * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
    

def gerar_de_dataset(path, ident=None):
    g = Digrafo(ident)
    with open(path+'.co','r') as arq:
        for e in arq.readlines():
            if e[0] == 'v':
                s = e.strip('v ').split(' ')
                g.add_ponto(int(s[0]),int(s[1]),int(s[2]))
                
    with open(path+'.gr','r') as arq:
        for e in arq.readlines():
            if e[0] == 'a':
                s = e.strip('a ').split(' ')
                g.add_arco(int(s[0]),int(s[1]),gerar_distancia(g,int(s[0]),int(s[1])))
    return g
   
def gerar_aleatoriamente(grid_x, grid_y, max_x, max_y, distancia_min, ident=None):
    grafo = Digrafo(ident)

    fracao_x, fracao_y = max_x/grid_x, max_y/grid_y
    tam_min_x = tam_min_y = distancia_min / 2
    tam_max_x, tam_max_y = fracao_x - tam_min_x, fracao_y - tam_min_y

    x_1, x_2, y_1, y_2 = tam_min_x, tam_max_x, tam_min_y, tam_max_y

    p_x = {i: (x_1 + fracao_x * (i + 1), x_2 + fracao_x * (i + 1)) for i in range(grid_x)}
    p_y = {i: (y_1 + fracao_y * (i + 1), y_2 + fracao_y * (i + 1)) for i in range(grid_y)}

    [grafo.add_ponto((key_x * _mult_ident_ponto) + key_y, uniform(x[0], x[1]), uniform(y[0], y[1]))
     for key_x, x in p_x.items() for key_y, y in p_y.items()]

    hor = []
    for i in range(grid_x):
        if i%2 == 0:
            hor += [i * _mult_ident_ponto + j for j in range(grid_y)]
        else:
            hor += [i * _mult_ident_ponto + j for j in reversed(range(grid_y))]

    ver = []
    for j in range(grid_y):
        if j%2 == 0:
            ver += [i * _mult_ident_ponto + j for i in range(grid_x)]
        else:
            ver += [i * _mult_ident_ponto + j for i in reversed(range(grid_x))]

    [grafo.add_arco(hor[i], hor[i + 1], gerar_distancia(grafo, hor[i], hor[i + 1])) for i in range(len(hor) - 1)]
    [grafo.add_arco(ver[i], ver[i + 1], gerar_distancia(grafo, ver[i], ver[i + 1])) for i in range(len(ver) - 1)]

    li = list(grafo.pontos)
    for i in range(len(grafo)//50):
        pt_a = li[randrange(len(li))]
        pt_b = li[randrange(len(li))]
        grafo.add_arco(pt_a, pt_b, gerar_distancia(grafo,pt_a,pt_b))

    return grafo

def gerar_distancia(grafo, pt_a, pt_b):
    distancia = 0
    while distancia < grafo.dist(pt_a, pt_b):
        distancia = round(grafo.dist(pt_a, pt_b) * uniform(1.0,1.5), 3)
        if distancia < grafo.dist(pt_a, pt_b):
            distancia += 0.05
    return distancia
