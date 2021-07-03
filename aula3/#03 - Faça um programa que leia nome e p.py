#03 - Faça um programa que leia nome e peso de várias pessoas,
#  guardando tudo em uma lista, depois do dado inserido, 
# pergunte ao usuário se ele quer continuar, 
# se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso
dados = []
maior = menor = 0
nomeMaior = nomeMenor = ''

while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    dados.append([nome, peso])
    continuar = input('\nVocê quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

for i in dados:
    if i[1] >= maior:
        maior = i[1]
        nomeMaior = i[0]
    if i[1] <= menor or menor == 0:
        menor = i[1]
        nomeMenor = i[0]
print(maior)
print(menor)