author = 'Eden Thiago Ferreira'
from statistics import *
from random import *
from grafos import *
from caminhos_minimos import *
from banco_dados import *

def coletar_normal():
    criar_se_nao_existe()
    con = Conexao()
    _x = randint(1000,2225)
    _y = randint(1000,2225)
    grafo = gerar_aleatoriamente(_x, _y, _x-500, _y-500, uniform(0.1,2), con.get_ident())
    print('grafo')
    con.inserir_grafo(grafo)

    pt_o, pt_d = sample(grafo.pontos, 2)
    dij = Dijkstra(grafo)
    dij.executar(pt_o, pt_d)
    ast = AStar(grafo)
    ast.executar(pt_o, pt_d)
    con.inserir_tabela_dijkstra(dij)
    con.inserir_tabela_astar(ast)
    del dij
    del ast

    pt_o, pt_d = sample(grafo.pontos, 2)
    dij = Dijkstra(grafo)
    dij.executar(pt_o, pt_d)
    ast = AStar(grafo)
    ast.executar(pt_o, pt_d)
    con.inserir_tabela_dijkstra(dij)
    con.inserir_tabela_astar(ast)
    del dij
    del ast

    pt_o, pt_d = sample(grafo.pontos, 2)
    dij = Dijkstra(grafo)
    dij.executar(pt_o, pt_d)
    ast = AStar(grafo)
    ast.executar(pt_o, pt_d)
    con.inserir_tabela_dijkstra(dij)
    con.inserir_tabela_astar(ast)
    del dij
    del ast
    del con

def imprimir_dados():
    con = Conexao()
    d = con.get_tempos_dijkstra_sem_caminho()
    a = con.get_tempos_astar_sem_caminho()
    with open('dicionario_dados.txt','w') as arq:
        print('Tempos dos Algoritmos',file=arq)
        print('                    Dijkstra                 A*',file=arq)
    with open('dicionario_dados.txt','a') as arq:
        for i in range(len(d['id'])):
            for key in d:
                if key != 'id':
                    if key == 'distancia_total':
                        print(key.rjust(15),' : ',str(round(d[key][i],3)).ljust(20),' : ', str(round(a[key][i],3)),file=arq)
                    else:
                        print(key.rjust(15),' : ',str(d[key][i]).ljust(20),' : ', str(a[key][i]),file=arq)
            print(file=arq)
