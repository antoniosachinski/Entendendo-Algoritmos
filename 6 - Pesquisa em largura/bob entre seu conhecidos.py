# funçãoq que verifica se há alguem chamado bob entre seu conhecidos e os conhecidos do conhecidos...
# criada com base na pesquisa em largura e verificavção de grafos
# exercício também usado pra explicação do conceito de fila (FIFO)

from collections import deque # importando a fila

grafo = {"bob" : ["any", "clara", "alice"], "any": ["jao", "bia", "tom"], "alice" : ["tim", "bruna", "ant", "aa"], "clara" : []}

def pesquisaLargura(grafo):
  fila = deque(grafo["bob"]) # 1. crie uma lista contendo todas a pessoas a serem classificadas
  while len(fila) > 0:
    pessoa = fila[0]
    fila.popleft() # 2. retire uma pessoa da fila

    if (pessoa == "bob"): # 3. confira se ela é o bob
      print("Você achou o bob!") # 3.2 sim!
    else:
      fila.extend(grafo.get(pessoa, [])) # 3.3 não! adiciona a rede dessa pessoa
  # 4. repita

pesquisaLargura(grafo)
