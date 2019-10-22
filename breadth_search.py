vizinhos = {
 'Arad':('Sibiu','Timisoara','Zerind'),
 'Zerind':('Arad','Oradea'),
 'Oradea':('Sibiu','Zerind'),
 'Timisoara':('Arad','Lugoj'),
 'Lugoj':('Mehadia','Timisoara'),
 'Mehadia':('Drobeta','Lugoj'),
 'Drobeta':('Craiova','Mehadia'),
 'Craiova':('Drobeta','Pitesti','Rimnicu'),
 'Sibiu':('Arad','Fagaras','Oradea','Rimnicu'),
 'Fagaras':('Bucareste','Sibiu'),
 'Rimnicu':('Craiova','Pitesti','Sibiu'),
 'Pitesti':('Bucareste','Craiova','Rimnicu'),
 'Neamt':('Iasi',),
 'Iasi':('Neamt','Vaslui'),
 'Vaslui':('Iasi','Urziceni'),
 'Bucareste':('Fagaras','Giurgiu','Pitesti','Urziceni'),
 'Giurgiu':('Bucareste',),
 'Urziceni':('Bucareste','Hirsova','Vaslui'),
 'Hirsova':('Eforie','Urziceni'),
 'Eforie':('Hirsova',),
}

distancias={
 'Arad':(140,118,75),
 'Zerind':(75,71),
 'Oradea':(151,71),
 'Timisoara':(118,111),
 'Lugoj':(70,111),
 'Mehadia':(75,70),
 'Drobeta':(120,75),
 'Craiova':(120,138,146),
 'Sibiu':(140,99,151,80),
 'Fagaras':(211,99),
 'Rimnicu':(146,97,80),
 'Pitesti':(101,138,97),
 'Neamt':(87,),
 'Iasi':(87,92),
 'Vaslui':(92,142),
 'Bucareste':(211,90,101,85),
 'Giurgiu':(90,),
 'Urziceni':(85,98,142),
 'Hirsova':(86,98),
 'Eforie':(86,),
}

def nosso_in(elemento,L):
    presente = False
    for i in range(len(L)):
        if elemento == L[i][0][-1]:
            presente = True
            break
    return presente

def objetivo(estado):
    return estado=='Bucareste'

def meu_criterio(x):
    return x[1]

estado_inicial = [['Arad'],0]

B = [] #fila
E = []

B.append(estado_inicial)
achei = False
while not achei:
  if (len(B)==0):
    break
  #B = sorted(B,key=meu_criterio)
  no = B[0][:]
  del B[0]
  E.append(no[0][-1])

  for vizinho in vizinhos[no[0][-1]]:
      if not nosso_in(vizinho,B) and not vizinho in E:
          e = vizinhos[no[0][-1]].index(vizinho)
          d = distancias[no[0][-1]][e]
          if objetivo(vizinho):
            no[0].append(vizinho)
            no[1] += d
            achei = True
            break
          B.append([ no[0] + [vizinho], no[1]+ d  ])


if achei:
  print (no)
else:
  print ('Nao achei.')
