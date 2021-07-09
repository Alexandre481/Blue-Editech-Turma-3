from hbomax import Hbomax
class Filme(Hbomax):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property 
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'''
        nome: {self.nome}      
        ano: {self.ano}
        duracao: {self.duracao}
        likes: {self.like}  
        '''
