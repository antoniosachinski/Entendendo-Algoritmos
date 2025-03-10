# função que calcula a soma dos elementos de uma lista utilizando recursão
# exercício proposto com o intuito de utilizar a recursão com uma alternativa ao "for", com base na ideia de dividir para conquistar

def soma(lista):
    if len(lista) == 0:  # caso base da recursão: se a lista estiver vazia
        return 0  # retorna 0, pois a soma de uma lista vazia é 0
    else:
        primeiroNumero = lista[0]  
        lista.remove(primeiroNumero)
        return soma(lista) + primeiroNumero  # chama recursivamente a função soma e adiciona o primeiro número à soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(soma(lista))  
