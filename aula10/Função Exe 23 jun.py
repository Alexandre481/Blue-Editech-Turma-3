# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# # A soma desses três parametros através de uma função.
# # Seu script também deve fornecer a média dos três números,  
# através de uma segunda função que chama a primeira.
def soma3(a, b, c):
    s = a + b + c
    return s


print('SOMA DE TRÊS NÚMEROS')
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))

print('Soma = ', soma3(a, b, c))
print('A média= ',soma3(a, b, c)/3:.2f)