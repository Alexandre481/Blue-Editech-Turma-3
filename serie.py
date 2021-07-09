from hbomax import Hbomax

class Serie (Hbomax):
    def __init__(self, ano, temporadas):
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f'''
        nome: {self.nome}      
        ano: {self.ano}
        temporadas: {self.temporadas}
        likes: {self.like}  
        '''
