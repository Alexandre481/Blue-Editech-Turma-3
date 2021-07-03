class pessoa:
    def __init__ (self, nome, idade,peso ): #metódo construtor/inicializador de atributos
        self.nomePessoa=nome
        self.idadePessoa=idade 
        self.pesoPessoa=peso

    def comer(self, calorias):
        self.pesoPessoa += calorias

    def malhar(self, calorias):
        self.pesoPessoa -= calorias

    def mostrarDados(self):   
        return f'''
        Nome={self.nomePessoa}
        Idade={self. idadePessoa}
        Peso= {self.pesoPessoa}
'''     

pessoa1=pessoa("Thiago",27,62.5)# Instanciar o objeto  um novo objeto
pessoa2=pessoa("Maria",34,70.0)# Instanciar o objeto  um novo objeto
   
pessoa1.mostrarDados() ###chamar  a classe
pessoa2.mostrarDados()

pessoa1.comer(5) ### CHAMAR ALTERAÇÃO ATRIBUTO
pessoa2.malhar(5)
print(pessoa1.mostrarDados())