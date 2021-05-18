### Exercicios Codelab n2
###Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois
#  seja maior que um terceiro parâmetro, chamado limite.
def soma_maior_que_limite(a, b, limite):
    if a + b > limite:
      return True
    else:
      return False

print(soma_maior_que_limite(82, 15, 60))