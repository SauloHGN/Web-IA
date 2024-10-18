from lista_dupla_encadeada import lista
import funcoes_auxiliares as fa


class busca(object):

    def amplitude(self, inicio, fim, mapa, dx, dy):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while not l1.vazio():
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            x = atual.estado[0]
            y = atual.estado[1]

            filhos = []
            filhos = fa.sucessor_grid(x,y,dx,dy,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return caminho
    
    def profundidade(self, inicio, fim, mapa, dx, dy):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while not l1.vazio():
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            x = atual.estado[0]
            y = atual.estado[1]

            filhos = []
            filhos = fa.sucessor_grid(x,y,dx,dy,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return caminho
    
    
    def prof_limitada(self, inicio, fim, mapa, dx, dy, limite):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while not l1.vazio():
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual.nivel<limite:
                x = atual.estado[0]
                y = atual.estado[1]
    
                filhos = []
                filhos = fa.sucessor_grid(x,y,dx,dy,mapa)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
    
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            #print("Árvore de busca:\n",l2.exibeLista())
                            return caminho

        return caminho
    
    def aprof_iterativo(self, inicio, fim, mapa, dx, dy, lim_max):

        for limite in range(1,lim_max):
            caminho = []
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while not l1.vazio():
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual.nivel<limite:
                    x = atual.estado[0]
                    y = atual.estado[1]
        
                    filhos = []
                    filhos = fa.sucessor_grid(x,y,dx,dy,mapa)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:
        
                        flag = True  # pressuponho que não foi visitado
        
                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.nivel+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.nivel+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.nivel + 1, atual)
                            l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                #print("Árvore de busca:\n",l2.exibeLista())
                                return caminho
    
    def custo_uniforme(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        caminho = []
        visitado = []
        print("inicio: ",inicio)
        print("fim: ",fim)
        l1.insereUltimoPT2(inicio,0,0,None)
        l2.insereUltimoPT2(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            print("atual: ", atual.estado)
            if atual.estado == fim:
                #caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                #return caminho, atual.valor2
                caminho[0]
                return caminho[::-1]

        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            
            #print("Novo: ",filhos)
            for novo in filhos:

                valor = [novo[0], novo[1]]
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2  # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == valor:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimoPT2(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"
    
    def greedy(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimoPT2(inicio,0,0,None)
        l2.insereUltimoPT2(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()

            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                #return caminho, atual.valor2
                caminho[0]
                return caminho[::-1]
        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = fa.h(valor,fim) # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimoPT2(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"
    
    def a_estrela(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimoPT2(inicio,0,0,None)
        l2.insereUltimoPT2(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                caminho[0]
                return caminho[::-1]
        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            
            
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 + fa.h(valor,fim) # f3(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.inserePos_X(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

    def aia_estrela(self,inicio,fim,mapa,dim_x,dim_y, limite):  
        
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            l1.insereUltimoPT2(inicio,0,0,None)
            l2.insereUltimoPT2(inicio,0,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                    caminho[0]
                    return caminho[::-1]
            
                filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
                
                for novo in filhos:
                    valor = []
                    valor.append(novo[0])
                    valor.append(novo[1])
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[1]  # custo do caminho
                    v1 = v2 + fa.h(valor,fim) # f3(n)
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==valor:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(valor, v1, v2, atual)
                            l2.insereUltimoPT2(valor, v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(valor)
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
            limite = float(sum(lim_exc)/len(lim_exc))
        return "Caminho não encontrado"


    
    # BUSCA BIDIRECIONAL
    def bidirecional(self, inicio, fim, mapa, dx, dy):
    
        # Primeiro Amplitude
        # Manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        
        # Segundo Amplitude
        # Manipular a FILA para a busca
        l3 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l4 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
    
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.primeiro().nivel:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                x = atual.estado[0]
                y = atual.estado[1]
    
                filhos = []
                filhos = fa.sucessor_grid(x,y,dx,dy,mapa)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            if visitado1[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado1[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==novo:
                                flag = True
                                break
                        
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.primeiro().nivel:
                    break
                
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
                x = atual.estado[0]
                y = atual.estado[1]
    
                filhos = []
                filhos = fa.sucessor_grid(x,y,dx,dy,mapa)
                
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            if visitado2[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado2[j][1]=atual.nivel+1
                            break
                        
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==novo:
                                flag = True
                                break
                            
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"