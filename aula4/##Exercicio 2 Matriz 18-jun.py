##Exercicio 2 Matriz 18-jun
# 02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

matriz = []
somaPar = soma3Coluna = 0

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input('Digite o valor: '))
        linha.append(valor)
        if valor % 2 == 0:
            somaPar += valor
    
    matriz.append(linha)

    soma3Coluna += linha[2]

for i in matriz:

    for j in i:
        print(f'   [ {j} ]', end='')

    print()

print(matriz)

print(f'A soma dos pares é {somaPar}')
print(f'A soma da terceira coluna é {soma3Coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')