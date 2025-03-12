# funçãoq que verifica se há alguem chamado bob entre seu conhecidos e os conhecidos do conhecidos...
# criada com base na pesquisa em largura e verificavção de grafos
# exercício também usado pra explicação do conceito de fila (FIFO)

from collections import deque # importando a fila

grafo = {"voce" : ["any", "clara", "alice"], "any": ["jao", "bia", "tom"], "alice" : ["tim", "bob", "bruna", "ant", "aa"], "clara" : []}

def pesquisaLargura(grafo):
  fila = deque(grafo["voce"]) # 1. crie uma lista contendo todas a pessoas a serem classificadas
  verificados = set() # lista para os já verificados
  
  while len(fila) > 0:
    pessoa = fila[0]
    fila.popleft() # 2. retire uma pessoa da fila
    
    if pessoa not in verificados:  # Vvê se a pessoa já foi verificada
      if (pessoa == "bob"): # 3. confira se ela é o bob
        print("Você achou o bob!") # 3.2 sim!
        return
    verificados.add(pessoa) # vai para a lista verificados
    fila.extend(grafo.get(pessoa, [])) # 3.3 não! adiciona a rede dessa pessoa
  # 4. repita
  
  print("bob não encontrado :(")

pesquisaLargura(grafo)
