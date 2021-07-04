# class Astronauta():
#     def __init__(self,nomeTripulante):
#         self.__nomeTripulante= nomeTripulante.title()

#     def __str__(self):
#         return self.__nomeTripulante
            
#     @property
#     def nomeTripulante(self):
#       return f'{self.__nomeTripulante}'

#     @nomeTripulante.setter
#     def nomeTripulante(self, nome):
#       self.__nomeTripulante = nome
#       return f' {self.__nomeTripulante}'

# nomes = []

# for i in range(4):
#     if i == 0:
#         nome = Astronauta(input("Você agora é o comandante,digite seu nome: "))
#     else:
#         nome = Astronauta(input(f"{nomes[0]},digite o centista {i}: "))
#     nomes.append(f'{nome}')
    
# print(nomes)
# # nome = Astronauta(input("Você agora é o comandante,digite seu nome: "))
# # print(f'{nome}')

import pygame
import os
pygame.init()
if os.path.exists('David Bowie - Starman-192k.mp3'):
  pygame.mixer.music.load('David Bowie - Starman-192k.mp3')
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(1)

  clock = pygame.time.Clock()
  clock.tick(10)

  while pygame.mixer.music.get_busy():
     pygame.event.poll()
     clock.tick(10)
else:
  print('O arquivo musica.mp3 não está no diretório do script Python')
