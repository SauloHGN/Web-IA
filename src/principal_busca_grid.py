import funcoes_auxiliares as fa
import funcoes_principais as mainFunc
from sys import exit

sol = mainFunc.busca()
caminho = []

# Busca em Grid
n = 30
m = 30
qt_ob = 8
if qt_ob>n*m:
    print("Erro!")
    exit()
else:
    for i in range(n):
        mapa = [[0 for _ in range(m)] for _ in range(n)]
        print(mapa[i])

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
destino = [5,2]
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