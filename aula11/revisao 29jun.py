# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica.
import random

class CaraCoroa:
 def __init__(self):
  self.lado = 'Cara'
  
 def lancar(self):
  if (random.randint(0,1))%2==0:
   self.lado = 'Deu Cara'
  else:
   self.lado = ' Deu Coroa'
  return self.lado

class Dado:
 def __init__(self):
  self.lado = 1
 def lancar(self):
  resultado =random.randint(1,6)   
  return  resultado

moeda = CaraCoroa()
dado = Dado()
op=1

while op:
 op=int(input("0.Sair:  "
       "1.Lançar Moeda: "
       "2.Lançar dado: "
))
    
 if op==1:
  print(moeda.lancar())
 elif op==2:
  print(f'Sua pontuação no jogo de dado foi: {dado.lancar()}')   

  