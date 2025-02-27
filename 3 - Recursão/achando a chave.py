# Função para procurar a string ()chave) dentro de uma lista (conjunto de caixa, possivelmtente com mais caixas dentro)
# A função utiliza recursão para lidar com listas dentro de listas

def procurarChave(listaCaixas):
  # Percorre cada elemento na lista fornecida
  for caractere in listaCaixas:
    if isinstance(caractere, str):
        print ("Você encontrou  chave:", caractere)  # Se for uma string, escreve o caractere encontrado
    elif isinstance(caractere, list):
        procurarChave(caractere)  # Caso o elemento seja uma lista, a função se chama recursivame

a = [0,[1,2,[3,4,5,[6,7,8,9,"A",10,11,12,13],14,15,16],17,18],19]
procurarChave(a)
