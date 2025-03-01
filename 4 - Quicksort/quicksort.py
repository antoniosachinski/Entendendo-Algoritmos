def quick(lista):
    if len(lista) < 2: # caso base da recursão: se a lista tiver menos de 2 elementos
        return lista # não há necessidade de ordenar, então simplesmente retorna a lista.
    else:
        # escolhendo o primeiro item da lista como o pivô
        pivo = lista[0]
        menores = []
        maiores = []

        # laço para percorrer os elementos da lista (exceto o pivô)
        for item in lista[1:]:
            # se o item for menor que o pivô, ele vai para a lista 'menores'
            if item < pivo:
                menores.append(item)
            # caso contrário, ele vai para a lista 'maiores'
            else:
                maiores.append(item)
        
        # a recursão chama o quick novamente para ordenar as listas 'menores' e 'maiores'
        # depois organiza o pivô no meio e retorna a lista ordenada
        return quick(menores) + [pivo] + quick(maiores)

a = [0, 1, 2, 3, 4, 5]
print(quick(a))
