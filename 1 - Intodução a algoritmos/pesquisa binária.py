# função que identifica a posição de um item em um array
# execício proposto no primeiro capítulo, com o intuito de explicar a lógica básica de um algoritimo e criar uma base para aplicação da notação Big O, quando comparamos pesquisa simples com pesquisa binária

def pesquisaBinaria (lista, item):
  baixo = 0
  alto = len(lista) - 1
  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute == item:
      return meio
    if chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None
minhaLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print (pesquisaBinaria(minhaLista, 7))
