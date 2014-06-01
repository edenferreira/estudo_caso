author = 'Eden Thiago Ferreira'
from random import *
from grafos import *
from caminhos_minimos import *
from banco_dados import *

def coletar_normal(repet):
    criar_se_nao_existe()
    con = Conexao()
    for i in range(repet):
        tam_grid = randint(800,1200)
        grafo = gerar_aleatoriamente(randint(1000,1500), randint(1000,1500), tam_grid, tam_grid, uniform(0.1,2), con.get_ident())
        pt_o, pt_d = sample(grafo.pontos, 2)
        dij = Dijkstra(grafo)
        dij.executar(pt_o, pt_d)
        ast = AStar(grafo)
        ast.executar(pt_o, pt_d)
        con.inserir_grafo(grafo)
        con.inserir_tabela_dijkstra(dij)
        con.inserir_tabela_astar(ast)
    del con