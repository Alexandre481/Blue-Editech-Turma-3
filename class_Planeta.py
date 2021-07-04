class Planeta():
    def __init__(self, nome, tipo):
        self.nome = nome.title()
        self.__ano = 0
        self.__consumo = 0
        self.tipo = tipo



    @property
    def tempo(self):
      return self.__tempo

    def tempo__gasto(self):
      self.__tempo += 1


    @property
    def combustivel(self):
      return self.__combustivel

#     def consumo__combustivel(self):
#       self.__combustivel += 1

# class Bios(Planeta): 
#    def __init__ (self, nome, tempo, combutivel, tipo):
#       super().__init__(nome, tempo, combutivel, tipo )
#       self.tempo = tempo
     
      
#    def imprime(self):
#      print(f'{self._nome} * {self.tempo} anos * {self.combustivel}  = {self._tipo}') 
  
      

class Agnostos(Planeta): 
   def __init__ (self, nome, tempo, combutivel, tipo):
      super().__init__(nome, tempo, combutivel, tipo )
      
   def imprime(self):
     print(f'{self._nome} * {self.tempo} anos * {self.combustivel}  = {self._tipo}') 

class Matér(Planeta): 
   def __init__ (self, nome, tempo, combutivel, tipo):
      super().__init__(nome, tempo, combutivel, tipo )

   def imprime(self):
     print(f'{self._nome} * {self.tempo} anos * {self.combustivel}  = {self._tipo}') 
   
      