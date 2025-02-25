# função que ordena um array do menor para o maior
# exercício proposto no segundo capítulo, denominado "Ordenação por seleção", dedicado a explicar sobre arrays e listas encadeadas.

def ordenarLista(lista):
  tamanhoLista = len(lista)
  listaOrdenada = []
  while tamanhoLista > 0:
    tamanhoLista -= 1
    maiorNumero = min(lista)
    lista.remove(maiorNumero)
    listaOrdenada.append (maiorNumero)
  return listaOrdenada

listaExemplo = [1,9,2,8,3,0,7,6,4,5]
print(ordenarLista(listaExemplo))
