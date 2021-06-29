# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista_temp=list()
jogos=list()
quant=int(input("Quantos jogos vc quer fazer?"))
for c in range(1,quant+1):
  cont=0
  while True:
     num=randint(1,6)
     if num not in lista_temp:
       lista_temp.append(num)
       cont +=1 
     if cont >=6:
      break
  lista_temp.sort()
  jogos.append(lista_temp[:])
  lista_temp.clear()
  print(f"\n -------{quant} jogos sendo sorteados -------")
  for i,c in enumerate(jogos):
     print(f"O {i+1}º jogo sorteado foi :{c}")
     sleep(1)