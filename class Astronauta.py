class Astronauta():
    def __init__(self,nomeTripulante):
        self.__nomeTripulante= nomeTripulante.title()

    def __str__(self):
        return self.__nomeTripulante
            
    @property
    def nomeTripulante(self):
      return f'{self.__nomeTripulante}'

    @nomeTripulante.setter
    def nomeTripulante(self, nome):
      self.__nomeTripulante = nome
      return f' {self.__nomeTripulante}'

nomes = []

for i in range(4):
    if i == 0:
        nome = Astronauta(input("Você agora é o comandante,digite seu nome: "))
    else:
        nome = Astronauta(input(f"{nomes[0]},digite o centista {i}: "))
    nomes.append(f'{nome}')
    
print(nomes)
# nome = Astronauta(input("Você agora é o comandante,digite seu nome: "))
# print(f'{nome}')