####Exerc 2 15-06.py
#####Crie um programa que pergunte ao usuário um número inteiro e faça a
####tabuada desse número.
tabuada=int(input("Qual a tabuada que você quer fazer: "))

for cont in range(1,11):
    print(f"{cont} x {tabuada}= {cont*tabuada}" )