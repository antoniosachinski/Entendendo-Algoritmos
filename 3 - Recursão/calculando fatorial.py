# função que identifica a posição de um item em um array
# execício proposto com o intuito de explicar a recursão, conceito onde uma função chama a si mesma para resolver um problema

numero = int(input("Digite um número para calcular o fatorial: "))
# estrutura básica de uma função recursiva:
def fatorial(numero):
  if (numero == 1): 
    return 1 # caso base: A condição de parada, onde a função não se chama novamente
    # sem o caso base, a recursão continuaria infinitamente 
  else:
    return numero * fatorial(numero - 1) # chamada Recursiva: A parte onde a função se chama novamente

print("O fatorial de", numero, "é", fatorial(numero))
