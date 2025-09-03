import heapq

def BuscaGulosaGrafo(grafo, inicio, objetivo, heuristica):
  fronteira = [] #fila de prioridade - lista de tuplas com (heuristica atual, no atual, caminho)

  heapq.heappush(fronteira, (heuristica[inicio], inicio, [inicio]))

  visitados = set() # Esse set() evita que haja repetição de nós, então ele sempre mantém o conjunto com elementos únicos.

  while fronteira != []:
    heuristica_atual, no_atual, caminho = heapq.heappop(fronteira) # Aqui ele pega o nó e o caminho da tupla que possui a menor heuristica.

    if no_atual == objetivo: # Se o nó atual for o objetivo, ele retorna o caminho.
      return caminho
    else: # Caso contrário, ele adiciona a lista de visitados.
      visitados.add(no_atual)

    for vizinho in grafo[no_atual]:
      if vizinho not in visitados: # Verifica se o vizinho já num foi visitado
        novo_caminho = caminho + [vizinho] # Caso não tenha sido, ele cria um novo caminho passando por ele.
        heapq.heappush(fronteira, (heuristica[vizinho], vizinho, novo_caminho)) # Aqui ele inclui na lista de prioridade de acordo com sua heuristica.

  return "Caminho não encontrado"

grafo = {'A': ['B', 'C'],
         'B': ['D', 'G'],
         'C': ['D', 'E'],
         'D': ['B','E','F'],
         'E': ['C','D','F'],
         'F': ['D','E','H'],
         'G': ['B','H'],
         'H': ['F','G'] }

heuristica = {'A': 6,
              'B': 4,
              'C': 3,
              'D': 5,
              'E': 1,
              'F': 5,
              'G': 3,
              'H': 0}

inicio = input("escolha o inicio: ").upper()
objetivo = input("escolha o objetivo: ").upper()

BuscaGulosaGrafo(grafo, inicio, objetivo, heuristica)

caminho_percorrido = BuscaGulosaGrafo(grafo, inicio, objetivo, heuristica)

if caminho_percorrido:
  print(caminho_percorrido)
else:
  print("Caminho não encontrado.")