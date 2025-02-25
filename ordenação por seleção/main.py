def ordenarLista(lista):
  tamanhoLista = len(lista)
  listaOrdenada = []
  while tamanhoLista > 0:
    tamanhoLista -= 1
    maiorNumero = min(lista)
    lista.remove(maiorNumero)
    listaOrdenada.append (maiorNumero)
  return listaOrdenada

listaEx = [1,9,2,8,3,0,7,6,4,5]
print(ordenarLista(listaEx))