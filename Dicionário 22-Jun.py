# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.  
grupo=list()
pessoa=dict()
while True:
    pessoa.clear()
    pessoa['nome']=str(input('nome:   '))
    while True:
        pessoa['sexo']=str(input('sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade']=int(input('idade:  '))
    grupo.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar?  [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp== 'N':
        break
print('-='*30)
print(grupo)