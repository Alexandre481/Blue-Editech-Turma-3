# Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.
lista_completa = [3, 7, 8, 11, 16, 20]
lista_pares = []
lista_impares = []

for c in lista_completa:
  if c % 2 == 0:
    lista_pares.append(c)
  else:
    lista_impares.append(c)

print(lista_impares)
print(lista_pares)
