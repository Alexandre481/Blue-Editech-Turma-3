#  Fazer o método sacar(), se o saldo for menor ou igual a 0, 
#  retorne uma mensagem dizendo que o saldo é insuficiente, 
#  caso o contrário, realize a operação de saque 
#  e mostre o saldo atual dessa conta;


class Conta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo  
        
    def __str__(self):
        if self.saldo == 0:
            return f'''
            titular: {self.titular}
            '''
        else:
            return f''' 
            titular: {self.titular}
            '''

    def depositar(self,valor):
        self.saldo += valor
        return f'''{self.titular} seu saldo atual é
        {self.saldo}'''

    def sacar(self, valor):
        if valor > 0:
            if self.saldo < valor:
                self.extrato()
                print (f'{self.titular} você  não tem R$ {valor:.2f} para sacar.')
        else:
            print('Você não pode sacar ZERO reais')
    def extrato(self):
        print(f'Seu saldo é: R$ {self.saldo:.2f}')


from  conta import Conta
if __name__ == '__main__':
    banco = list()
    while True:
        conta = conta(input('titular:  '))
        banco.append(conta)

        resp = input('Deseja continuar? [S,N]').upper().strip()[0]
        if resp == 'N':
            break

    print(banco[1].depositar(50))

@property
def saldo (self):
    return self._saldo

@saldo.setter
def saldo(self, saldo):
    self.__saldo = saldo    

@property
def titular (self):
    return self.titular

@saldo.setter
def titular(self, titular):
    self.__titular = saldo    

    