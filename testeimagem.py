import turtle
import pygame
import os
pygame.init()
if os.path.exists('Interstellar Soundtrack by  Hans Zimmer (320  kbps).mp3'):
  pygame.mixer.music.load('Interstellar Soundtrack by  Hans Zimmer (320  kbps).mp3')
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(1)

  clock = pygame.time.Clock()
  clock.tick(10)

#   while pygame.mixer.music.get_busy():
#      pygame.event.poll()
#      clock.tick(10)
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
t= turtle.Pen()
 
t.speed(5)
 
turtle.bgcolor("black")
 
for x in range(200):
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 
 
turtle.done()
t.speed(5)
 
turtle.bgcolor("black") 
 
for x in range(200):
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 
 
turtle.done()

# import pygame
# import os
# pygame.init()
# if os.path.exists('David Bowie - Starman-192k.mp3'):
#   pygame.mixer.music.load('David Bowie - Starman-192k.mp3')
#   pygame.mixer.music.play()
#   pygame.mixer.music.set_volume(1)

#   clock = pygame.time.Clock()
#   clock.tick(10)

#   while pygame.mixer.music.get_busy():
#      pygame.event.poll()
#      clock.tick(10)
# else:
#   print('O arquivo musica.mp3 não está no diretório do script Python')
