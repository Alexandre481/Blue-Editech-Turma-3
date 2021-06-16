#####Crie um programa que leia a idade e o sexo de várias pessoas. A cada
#####pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
####continuar. No final, mostre:
#####A) Quantas pessoas têm mais de 18 anos.
#####B) Quantos homens foram cadastrados.
#####C) Quantas mulheres têm menos de 20 anos.
m = d18 = m20 =0
while True:
    i = int(input('Idade: '))
    s = a = ' '
    while s not in 'FM':
        s = str(input('Sexo[F/M]: ')).strip().upper()[0]
    if i > 18:
        d18 += 1
    if s in 'M':
        m += 1
    if s in 'F' and i < 20:
        m20 += 1
    while a not in 'SN':
        a = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if a == 'N':
        break
print(f'Pessoas com mais de 18 anos: {d18}')
print(f'Número de homens cadastrados: {m}')
print(f'Mulheres com menos de 20 anos: {m20}')