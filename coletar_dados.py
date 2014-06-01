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

        imprimir_dados()

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
                    print(key.rjust(15),' : ',str(d[key][i]).ljust(20),' : ', str(a[key][i]),file=arq)
            print(file=arq)