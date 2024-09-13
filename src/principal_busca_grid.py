import sys
import os

# Adiciona o diretório 'src' ao sys.path se não estiver lá
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')

if src_dir not in sys.path:
    sys.path.append(src_dir)

import funcoes_auxiliares as fa
import funcoes_principais as mainFunc
from sys import exit

sol = mainFunc.busca()
caminho = []

imagens = {
    0: 'chao.png',
    1: 'destino.png',
    9: 'obstaculo.png',
    7: 'origem.png'
}

# Busca em Grid
n = 20
m = 40
qt_ob = 10

"""
origem = []
destino = []
print("Origem:")
origem.append(int(input("X = ")))
origem.append(int(input("Y = ")))
print("Destino:")
destino.append(int(input("X = ")))
destino.append(int(input("Y = ")))
"""
origem = [3,2]
destino = [0,0]


if qt_ob>n*m:
    print("Erro!")
    exit()
else:
    mapa = fa.Gera_Problema_Grid(n,m,qt_ob)
    mapa[destino[0], destino[1]] = 1
    for i in range(n):
        print(mapa[i])


print(origem,destino)

# Pontos fora dos limites
if origem[0]<0 or origem[1]<0 or destino[0]<0 or destino[1]<0 or origem[0]>=n or origem[1]>=m or destino[0]>=n or destino[1]>=m:
    print("Origem ou destino fora do limite")
    exit()

# Pontos igual a obstáculo
if mapa[origem[0]][origem[1]]==9 or mapa[destino[0]][destino[1]]==9:
    print("Origem ou destino é igual a obstáculo")
    exit()

caminho = sol.amplitude(origem,destino,mapa,n,m)
print("\n============== AMPLITUDE ==============")
print("Caminho: ",caminho)
print("Custo:",len(caminho)-1)

caminho = sol.profundidade(origem,destino,mapa,n,m)
print("\n============== PROFUNDIDADE ==============")
print("Caminho: ",caminho)
print("Custo:",len(caminho)-1)

limite = 10
caminho = sol.prof_limitada(origem,destino,mapa,n,m,limite)
print("\n============== PROFUNDIDADE LIMITADA ==============")
print("Caminho: ",caminho)
print("Custo:",len(caminho)-1)

lim_max = 20
caminho = sol.aprof_iterativo(origem,destino,mapa,n,m,lim_max)
print("\n============== APROFUNDAMENTO ITERATIVO ==============")
print("Caminho: ",caminho)
print("Custo:",len(caminho)-1)

caminho = sol.bidirecional(origem,destino,mapa,n,m)
print("\n============== BIDIRECIONAL ==============")
print("Caminho: ",caminho)
print("Custo:",len(caminho)-1)