# programa com a função de exemplificar o uso dos dicionários em python (tabela hash)
# funcionamento do programa: quatro jogadores jogam um dado e conseguem resultados aleatorios, que depois serão organizados e o vencedor será o com maior númer no dado, tudo utilizando dicionários

from random import randint # importando a modúlo para o dado
from operator import itemgetter
print("Calculando os valores para cada jogador:")
jogadas = {}
jogadas ["jogador1"] = randint(1,6)
jogadas ["jogador2"] = randint(1,6)
jogadas ["jogador3"] = randint(1,6)
jogadas ["jogador4"] = randint(1,6)

print("Valores sorteados:") # exibindo valores para cada jogador
for jogador, numero in jogadas.items(): 
  print("O {} jogou {}" . format (jogador, numero))

ranking = sorted(jogadas.items(), key = itemgetter (1), reverse  = True) # ordenando dicionario a partir dos valores do dado e atribuindo a uma lista

print("Ranking:") # exibindo valores ordenados
for variavel, jogador in enumerate(ranking): 
  print(f"{variavel + 1}° lugar: {jogador[0]} com {jogador[1]}.")
