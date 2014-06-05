author = 'Eden Thiago Ferreira'
#from statistics import *
from random import *
from grafos import *
from caminhos_minimos import *
from banco_dados import *
from pprint import pprint

def coletar_normal():
    criar_se_nao_existe()
    con = Conexao()
    _x = randint(1000,1500)
    _y = randint(1000,1500)
    grafo = gerar_aleatoriamente(_x, _y, _x//2, _y//2, uniform(0.1,2), con.get_ident())
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
    with open(r'dicionario_dados.txt','w') as arq:
        print('Tempos dos Algoritmos',file=arq)
        print('                    Dijkstra                 A*',file=arq)
    with open(r'dicionario_dados.txt','a') as arq:
        for i in range(len(d['id'])):
            for key in d:
                if key != 'id':
                    if key == 'distancia_total':
                        print(key.rjust(15),' : ',str(round(d[key][i],3)).ljust(20),' : ', str(round(a[key][i],3)),file=arq)
                    else:
                        print(key.rjust(15),' : ',str(d[key][i]).ljust(20),' : ', str(a[key][i]),file=arq)
            print(file=arq)

def recuperar_dados():
    con = Conexao()
    d = con.get_tempos_dijkstra()
    a = con.get_tempos_astar()
    with open('dijkstra.txt','w') as arq:
        for e in d:
            for f in e:
                if f != e[5]:
                    print(f,end=',',file=arq)
            print(file=arq)
    with open('astar.txt','w') as arq:
        for e in a:
            for f in e:
                if f != e[5]:
                    print(f,end=',',file=arq)
            print(file=arq)
