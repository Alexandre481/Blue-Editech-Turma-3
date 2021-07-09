from typing_extensions import TypeVarTuple
from serie import Serie
from filme import Filme
Catalogo = list()
while True:
    cadastro = input("O que vc quer cadastrar? [Filme/Serie").strip().upper()[0]
    
    if cadastro == 'F':
        filme = Filme(
            input ('Nome: '),
            int(input('Ano: ')),
            int(input('Duracao: '))
        )
        catalago.append(serie)
    elif cadastro == 'S':
        serie = Serie(
            input('Nome: ')
            int(input('Ano: ')),
            int(input('Temporadas: '))
            )

    continua = input('Você quer continuar? [S/N]: ')
    while continua not in 'SN':
        continua = input('Você quer continuar? [S/N]: ')
    if continua == 'N':
        break

    for i in catalogo:
        print(i)
        like = input("Você quer dar likes? [S,N] ")
        while like not in 'SN':
            like = input('Você quer dar um like neste item? ['S/N'] ')