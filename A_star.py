from heapq import heappush, heappop
import time

"""
=======================
Considere o quebra-cabeca do bloco deslizante contendo 8 pecas, como ilustrado 
abaixo. Implemente o algoritmo A* para resolvê-lo. O programa deve permitir a entrada dos estados 
inicial e objetivo.
========================

- O módulo heapq foi utilizado para implementar uma lista de prioridade
- A primeira parte do código contém as funções relacionadas ao puzzle.
- A segunda parte contém as funções relacionadas ao algoritmo de ordenação A* e 
sua implementação para resolve o puzzle proposto pelo exercício.
- O que cada função faz, está logo acima da sua definição.
- Alguns passos do algoritmo foram comentados para facilitar a compreensão.
"""

###############   PARTE UM   ################

#digitar: usada para receber o estado inicial e o objetivo
def digitar():
    lista = []
    A = input()
    A = A.split(" ")
    for j in range (9):
        lista.append(int(A[j]))
    return lista

print("\n######## 8-PUZZLE #########")
print("--> Por favor digite o estado inicial do 8-puzzle:")
print("Exemplo: 7 2 4 5 0 6 8 3 1")

estado_inicial = digitar()
estado = [0,0,[estado_inicial]]

print("--> Por favor digite o estado objetivo do 8-puzzle:")
obj = digitar()


#imprime : imprime o estado
def imprime(lista):
    print('--------------')
    for i in range(len(lista)):
            print("|{: d}".format(lista[i]), end = " ")
            if (i+1)%3 == 0: 
                print("|") 
                
#verifica se é o objetivo
def objetivo(estado, objetivo):
    return estado== objetivo
    
#onde: encntra a linha e a coluna de um item em um estado
def onde(lista,item):
    index = lista.index(item)
    if index in [0,1,2]: return 0, [0,1,2].index(index)
    elif index in [3,4,5]: return 1, [3,4,5].index(index)
    elif index in [6,7,8]: return 2,  [6,7,8].index(index)
        
#manhattan : calcula a heurística de manhattan(soma das peças até suas posições)
def manhattan(lista,objetivo):
    dist = 0
    for item in range(1,9):
        linha_lista, coluna_lista = onde(lista, item)
        linha_obj,coluna_obj = onde(objetivo, item)
        dist += abs(linha_lista-linha_obj)+abs(coluna_lista-coluna_obj)
    return dist

#movimentos : retorna os possíveis estados de um estado
def movimentos(estado):
    index = estado.index(0)
    estados =[]
    if index in [3,4,5,6,7,8]:
        lista = estado[:]
        lista[index-3], lista[index] = lista[index], lista[index-3]
        estados.append(lista)
    if index in [0,1,2,3,4,5]:
        lista = estado[:]
        lista[index+3], lista[index] = lista[index], lista[index+3]
        estados.append(lista)
    if index in [0,1,3,4,6,7]:
        lista = estado[:]
        lista[index+1], lista[index] = lista[index], lista[index+1]
        estados.append(lista)
    if index in [1,2,4,5,7,8]:
        lista = estado[:]
        lista[index-1], lista[index] = lista[index], lista[index-1]
        estados.append(lista)
    return estados
    

############ PARTE DOIS #########################
  
#opcao_in : função utilizada para verficar se um estado está na borda
def opcao_in(elemento,L):
    presente = False
    for i in range(len(L)):
        if elemento == L[i][-1][-1]:
            presente = True
            break
    return presente
    
#retorna o índice de dado estado na borda
def in_B(estado, B):
    for i in range(len(B)):
        if estado == B[i][-1][-1]:
            return i
#def busca(estado):
B = []
E = []

heappush(B,estado)

achei = False
inicio = time.time()
while not achei:
    if (len(B)==0):
        break
    #prioridade recebe uma tupla com: f(n), custo, nó 
    prioridade = heappop(B)
    no = prioridade[-1]
    #no[-1] corresponde ao que chamamos de estado atual
    E.append(no[-1])
    #verfica se o último estado do nó é o objetivo
    if objetivo(no[-1], obj):
        achei = True
        break
    estados = movimentos(no[-1])
    custo = prioridade[1] + 1
    for estado in estados:
        #adicionar: adiciona um estado ao nó atual
        adicionar = no + [estado]
        #fn : calcula a distância de manhattan e adiciona o custo
        fn = manhattan(estado,obj)+custo
        if not opcao_in(estado,B):
            if not estado in E:
                  #coloca em uma fila de prioridade
                  # adiciona na borda(B) a heurística + custo e o nó
                heappush(B,(fn,custo,adicionar))
            #se o estado está na borda   
            elif opcao_in(estado, B):
                borda = in_B(estado, B)
                # se está na borda com maior custo, subtitui o nó 
                #pelo no com o estado atual
                if B[borda][0] > fn:
                    B[borda] = (fn, custo, adicionar)
            
                 


if achei:
    final = time.time()
    for i in no:
        imprime(i)
    print("\nO puzzle foi resolvido em {:d} passos".format(prioridade[1]))
    print("O tempo foi : {:.2f}s".format(final-inicio))
else:
    print ('Nao achei.')
    print(prioridade)
