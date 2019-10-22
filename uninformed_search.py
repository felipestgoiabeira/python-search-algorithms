"""
======================
Considere o seguinte cenário: \um fazendeiro esta levando uma raposa, uma galinha e um saco
de gr~aos para casa. Para chegar lá, ele precisa atravessar um rio de barco. Só que ele pode levar consigo
apenas um item de cada vez. Se a raposa for deixada sozinha com a galinha, ela comera a galinha. Se
a galinha for deixada sozinha com os grãos, ela comerá os grãos. Como o fazendeiro poderá atravessar
o rio mantendo todo seu suprimento intacto?". Esta situação pode ser modelada como um problema de
busca. Implemente um algoritmo de busca sem informação que resolva o problema, retornando como resposta
a sequência de acões necessárias para alcancar o estado objetivo a partir do estado inicial.
========================
"""
#foi utilizado uma lista para respresentar o estado
estado_inicial = [["fazendeiro","galinha" ,"saco", "raposa", "*RIO*"] ]

# passa o fazendeiro do lado 1 para lado 2
def passar_rio(onde,no):
    estado= no[:]
    passar = estado.pop(onde)
    estado.append(passar)
    return estado

#passa o fazendeiro do lado 2 para lado 1
def voltar_rio(onde,no):
    estado = no[:]
    passar = estado.pop(onde)
    estado = [passar]+ estado
    return estado

#verifica se dois objetos estão juntas e sem o fazendeiro
def juntos(lista, a, b):
    cont = 0
    for i in range(len(lista)):
        if lista[i] == a or lista[i]== b and not "fazendeiro" in lista:
            cont += 1
    if cont == 2: return True
    return False
    
# passando o lado 1 e lado2 como parâmetros verifica se os objetos estão juntos
def restricoes(lista1, lista2):
    if not juntos(lista1,"galinha", "raposa"):
        if not juntos(lista2,"galinha", "raposa"):
            if not juntos(lista1,"galinha", "saco"):
                    if not juntos(lista2,"galinha", "saco"):
                        return True
    return False
# o *RIO* como primeiro elemento da lista foi colocado como objetivo
def objetivo(a):
    if a[0] == "*RIO*":
            return True
    return False

#verifica se os lados correspondem as restrições dadas no exercícios
def verifica_lados(no):
    rio = no.index("*RIO*")
    lado1 = [no[item] for item in range(rio) ]
    lado2 = [no[item] for item in range(rio+1, 6) if item < 5]
    if restricoes(lado1,lado2):
        return True
    return False

#gera as escolhas possíveis
def escolhas(no):
    opcoes =[]
    rio = no.index("*RIO*")
    fazendeiro = no.index("fazendeiro")
    # se o fazendeiro esta do lado1 ele pode levar alguma coisa
    if fazendeiro < rio:
        estado = passar_rio(fazendeiro,no)
        for i in range(rio-1):
            levar= passar_rio(i,estado)
            if verifica_lados(levar):
                    opcoes.append(levar)
    #se o fazendeiro esta do lado2
    if fazendeiro > rio or opcoes == []:
        trazer = voltar_rio(fazendeiro,no)
        rio = trazer.index("*RIO*")
        #verifica se ele pode voltar
        if verifica_lados(trazer):
            opcoes.append(trazer)
        # verifica se ele pode trazer algo
        for i in range(4, rio ,-1):
            levar = voltar_rio(i,trazer)
            if verifica_lados(levar):
                opcoes.append(levar)
        #verifica se ele pode voltar e levar algo
        if verifica_lados(trazer):
            fazendeiro = trazer.index("fazendeiro")
            trazer = passar_rio(fazendeiro,trazer)
            for i in range(rio-1):
                levar= passar_rio(i,trazer)
                if verifica_lados(levar):
                    opcoes.append(levar)
    return opcoes

# verifica se dada opção está no conjunto explorado
def opcaoin_E(teste, Ex):
    opcao = teste[:]
    rio_opcao = opcao.index("*RIO*")
    lado_opcao =  [opcao[item] for item in range(rio_opcao) ]
    lado_opcao.sort()
    for testar in Ex:
        explorado = testar[:]
        rio_explorado = explorado.index("*RIO*")
        lado_explorado =  [explorado[item] for item in range(rio_explorado) ]
        lado_explorado.sort()
        if lado_opcao == lado_explorado:
            return True
    return False
    
# verifica de dada opção está na Borda
def opcaoin_B(teste, B):
    opcao = teste[:]
    rio_opcao = opcao.index("*RIO*")
    lado_opcao =  [opcao[item] for item in range(rio_opcao) ]
    lado_opcao.sort()
    for i in range(len(B)):
        borda = B[i][-1][:]
        rio_borda = borda.index("*RIO*")
        lado_borda =  [borda[item] for item in range(rio_borda) ]
        lado_borda.sort()
        if lado_opcao == lado_borda:
            return True
    return False


B = []
E = []
B.append(estado_inicial)
achei = False

while not achei:
    if (len(B)==0):
        break
    no = B[0][:]
    del B[0]
    E.append(no[-1])
    #gera as opções de cada nó
    opcoes = escolhas(no[-1])
    for opcao in opcoes:
        #verifica se o nó não está na borda ou conjunto explorado
        if not opcaoin_B(opcao,B):
            if not opcaoin_E(opcao,E) :
                if objetivo(opcao):
                    no.append(opcao)
                    achei = True
                    break
                adicionar = no +[opcao]
                #adciona o nó na borda
                B.append(adicionar)


if achei:
    j = 1
    for i in no:
        print("O estado %d é: " %j,i)
        j += 1

else:
    print("Não achei")

        
