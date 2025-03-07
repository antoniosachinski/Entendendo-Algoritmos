# função que cria uma tabela de multiplicação com todos os elementos do array

def tabelaMultiplicação(lista): 
  for item in lista: # laço externo
    for item2 in lista: # laço interno
      print(item2 * item, end="\t")  # imprime o resultado, com tabulação 
    print()  # quebra de linha após cada linha

lista = [0,1,2,3,4,5,6,7,8,9]
tabelaMultiplicação(lista)
