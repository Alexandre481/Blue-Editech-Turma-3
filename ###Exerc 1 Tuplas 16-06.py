###Exerc 1  Tuplas 16-06
#####01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50
#  e colocar em uma  tupla.
#####Depois disso, mostre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.
# # Sem utilizar repetições.
####Dica: utilizar a biblioteca random do Python.


from random import sample

num = tuple(sample(range(50), 5))
for i in num:
    print(i, end=' ')
print(f'''
Maior valor sorteado: {max(num)}
Menor valor sorteado: {min(num)}.''')
