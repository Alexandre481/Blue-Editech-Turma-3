###Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
####o maior e o menor peso lidos.
import math
maior = 0
menor = 1000
for c in range(1, 6):
    p = int(input("Digite o peso da  pessoa em Kg: "))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print(f"O menor peso são {menor} Kg e o maior peso é {maior}Kg")

