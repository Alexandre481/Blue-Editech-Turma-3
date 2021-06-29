# Faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def pn(n):
    if n > 0:
        print('P')
    elif n == 0:
        print('N')
    else:
        print('N')

print('POSITIVO OU NEGATIVO')
n = int(input('digite um número: '))
print('Este número é', end=' ')
pn(n)

