# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.
s = c1000 = cont = menor = 0
nome = ' '
while True:
    cont += 1
    p = float(input('Preço: '))
    n = str(input('Nome: ')).strip().capitalize()
    s += p
    if p > 1000:
        c1000 += 1
    if cont == 1 or p < menor:
        menor = p
        nome = n
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar [S/N]? ')).strip().upper()
    if c == 'N':
        break
print(f'Total gasto: {s}')
print(f'Produtos mais de R$1000: {c1000}')
print(f'O produto mais barato é: {nome}')