# função que ordena um array do menor para o maior
# exercício dedicado a explicar sobre arrays e listas encadeadas

def ordenarLista(lista):
  listaOrdenada = []
  while lista:
    menorNumero = min(lista)
    lista.remove(menorNumero)
    listaOrdenada.append (menorNumero)
  return listaOrdenada

listaExemplo = [88,33,47,76,20,31,74]
print(ordenarLista(listaExemplo))
