# Faça um programa, com uma função que necessite de um argumento. A função retorna
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
# negativo e ‘0’ se for 0.
def numero_real(n1):
    if n1 > 0:
        return 'Este numero é positivo'
    elif n1 < 0:
        return 'Este numero é negativo'
    else:
        return 'Este numero é igual a zero'
continuar=True
while continuar==True:
    usuario = int(input('Digite um numero:  ')) 
    print(numero_real(usuario))
    pergunta=input('Deseja continuar?:').strip().upper()
    if pergunta.startswith('S'):
        continuar = True
    else:
        continuar = False
print('Obrigado por jogar')