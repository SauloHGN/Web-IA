import copy
import math
from flask import Flask, render_template, redirect, request, url_for
from src.principal_busca_grid import imagens, inicializarDados

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global sol, caminho, n, m, qt_ob, origem, destino, mapa, mapa_original, algoritmo, sol2
    algoritmo = None
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        
        if form_type == 'draw-map':
            # Inicializar variáveis comuns para ambos os formulários
            origem = [int(request.form['origem_x']), int(request.form['origem_y'])]
            destino = [int(request.form['destino_x']), int(request.form['destino_y'])]

            if origem == destino:
                return "As coordenadas de origem e destino devem ser diferentes"

            sol, caminho, n, m, qt_ob, origem, destino, mapa  = inicializarDados(origem, destino)

            mapa[origem[0], origem[1]] = 7 # insere origem
            mapa[destino[0], destino[1]] = 1 # insere destino

            mapa_original = copy.deepcopy(mapa)

            if origem[0] < 0 or origem[1] < 0 or destino[0] < 0 or destino[1] < 0 or origem[0] >= n or origem[1] >= m or destino[0] >= n or destino[1] >= m:
                return "Origem ou destino fora do limite", 400

            if mapa[origem[0]][origem[1]] == 9 or mapa[destino[0]][destino[1]] == 9:
                return "Origem ou destino é igual a obstáculo", 400
            

            return render_template('index.html', matriz=mapa, imagens=imagens, caminho=caminho, custo=len(caminho)-1, mostrar_mapa=True, caminho_encontrado = False, algoritmo = algoritmo)

        elif form_type == 'run_algorithm':
            if 'mapa_original' not in globals():
                return "É necessario preencher os dados e gerar o mapa antes de executar o algoritmo."
           
            algoritmo = request.form['algoritmo']
            mapa = copy.deepcopy(mapa_original)

            if algoritmo == 'amplitude':
                caminho = sol.amplitude(origem, destino, mapa, n, m)
                print("\n============== AMPLITUDE ==============")
                
            elif algoritmo == 'profundidade':
                caminho = sol.profundidade(origem, destino, mapa, n, m)
                print("\n============== PROFUNDIDADE ==============")

            elif algoritmo == 'prof_limitada':
                limite = math.fabs(origem[0] - destino[0]) + math.fabs(origem[1] - destino[1])
                print("LIMITE", limite)
                caminho = sol.prof_limitada(origem, destino, mapa, n, m, limite)
                print("\n============== PROFUNDIDADE LIMITADA ==============")

            elif algoritmo == 'aprof_iterativo':
                lim_max = math.ceil(math.fabs(origem[0] - destino[0]) + math.fabs(origem[1] - destino[1]))
                caminho = sol.aprof_iterativo(origem, destino, mapa, n, m, lim_max)
                print("\n============== APROFUNDAMENTO ITERATIVO ==============")

            elif algoritmo == 'bidirecional':
                caminho = sol.bidirecional(origem, destino, mapa, n, m)
                print("\n============== BIDIRECIONAL ==============")

            
             #----------------- Algoritmos parte 2 ------------------
            elif algoritmo == 'custoUniforme':
                caminho = sol.custo_uniforme(origem, destino, mapa, n, m)
                print("\n============= CUSTO UNIFORME ==============")
                print("Caminho: \n",caminho)
                print("Custo:",len(caminho)-1)

            elif algoritmo == 'greedy':
                caminho = sol.greedy(origem, destino, mapa, n, m)
                print("\n================ GREEDY =================")
                print("Caminho: \n",caminho)
                print("Custo:",len(caminho)-1)

            elif algoritmo == 'aEstrela':
                caminho = sol.a_estrela(origem, destino, mapa, n, m)
                print("\n============== A ESTRELA ===============")
                print("Caminho: \n",caminho)
                print("Custo:",len(caminho)-1)


            elif algoritmo == 'aia_estrela':
                lim_max = math.ceil(math.fabs(origem[0] - destino[0]) + math.fabs(origem[1] - destino[1]))
                caminho = sol.aia_estrela(origem, destino, mapa, n, m, lim_max)
                print("\n============= AIA ESTRELA ==============")
                print("Caminho: \n",caminho[0])
                print("Custo:",len(caminho)-1)


            else:
                return "Algoritmo desconhecido", 400

            print("Caminho: ", caminho)
            print("Custo:", len(caminho) - 1)

            mapaAtualizado = mapa
            mapaAtualizado = updateMap(mapa, caminho)
            return render_template('index.html', matriz=mapaAtualizado, imagens=imagens, caminho=caminho, custo=len(caminho)-1, mostrar_mapa=True, caminho_encontrado = True, algoritmo = algoritmo)

    return render_template('index.html', mostrar_mapa= False, caminho_encontrado = False, algoritmo = algoritmo)

# @app.route('/<path:subpath>', methods=['GET'])
# def redirecionar(subpath):
#     return redirect(url_for('index'))  # Alterado de 'home' para 'index'

def updateMap(mapa, caminho):
    mapaAtualizado = mapa
    if(caminho == 'Caminho não encontrado'):
        return 'OPs...'
    if len(caminho) > 2:
        for coordenada in caminho[1:-1]:
            x, y = coordenada
            if 0 <= x < mapaAtualizado.shape[0] and 0 <= y < mapaAtualizado.shape[1]:
                mapaAtualizado[x, y] = 2
    else:
        for coordenada in caminho[1:-1]:
            x, y = coordenada
            if 0 <= x < mapaAtualizado.shape[0] and 0 <= y < mapaAtualizado.shape[1]:
                mapaAtualizado[x, y] = 2

    return mapaAtualizado

        





if __name__ == '__main__':
    app.run(debug=True)
