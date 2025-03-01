# função que ordena uma lista utilizando o algoritmo Quicksort
# exercício proposto com o intuito de explicar a recursão e o conceito de dividir para conquistar

def quick(lista):
    if len(lista) < 2: # caso base da recursão: se a lista tiver menos de 2 elementos
        return lista # não há necessidade de ordenar então simplesmente retorna a lista
    else:
        pivo = lista[0] # escolhendo o primeiro item da lista como o pivô
        menores = []
        maiores = []
        for item in lista[1:]: # laço para percorrer os elementos da lista (exceto o pivô)
            if item < pivo: # se o item for menor que o pivô, ele vai para a lista 'menores'
                menores.append(item)
            else: # caso contrário, ele vai para a lista 'maiores'
                maiores.append(item)
        return quick(menores) + [pivo] + quick(maiores) # a recursão para ordenar as listas 'menores' e 'maiores'

a = [0, 1, 2, 3, 4, 5]

print(quick(a))
