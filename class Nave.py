class Nave():
    def __init__(self, nome):
        self.__nome = nome.title()
        self.__combustivel = 100
    def __str__(self):
        return f'{self.nome}'   
        

        
    @property
    def nome(self):
      return self.__nome

    @nome.setter
    def nome(self, nome):
      self.nome = nome
      return self.nome 
