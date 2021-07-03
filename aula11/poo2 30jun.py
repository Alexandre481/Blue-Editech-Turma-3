


from conta import Conta
if __name__ == '__main__':
    banco = list()
    while True:
        conta = Conta(input('titular:  '))
        banco.append(conta)

        resp = input('Deseja continuar? [S,N]').upper().strip()[0]
        if resp == 'N':
            break

    print(banco[1].depositar(50))

    for o in banco:
        print(o)    