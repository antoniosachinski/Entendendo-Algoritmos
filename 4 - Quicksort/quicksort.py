def quick(lista):
  if len(lista) < 2:
    return lista
  else:
    pivo = lista[0]
    menores = []
    maiores = []
    for item in lista[1:]: 
      if item < pivo:
        menores.append(item)
      else:
        maiores.append(item)
  return quick(menores) + [pivo] + quick(maiores)

a = [0,1,2,3,4,5]
print(quick(a))