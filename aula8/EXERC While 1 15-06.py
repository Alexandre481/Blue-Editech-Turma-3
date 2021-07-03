# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior 
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
d = 0
while d != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    d = int(input('Escolha sua opção: '))
    if d == 1:
        print('A soma é: {}'.format(n1+n2))
    elif d == 2:
        print('A multiplicação é: {}'.format(n1*n2))
    elif d == 3:
        if n1 > n2:
            print('O maior é: {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif d == 4:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    else:
        print('Número inválido.Por favor digite novamente:')
print('Fim do programa')