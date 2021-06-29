# Projeto 3- Jogo de Dados.
# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
# jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande
# campeão.

# para as rodadas vai ser for
# pq é uma quantidade limitada
# agora, se vc quiser perguntar no final do programa se ele quer jogar de novo,
#  vai ter que ser while
# e o for vai dentro do while
# igual no projeto 2


from random import randint
from time import sleep
from operator import itemgetter
rodadas=int(input('Quantas rodadas você deseja jogar?:'))
while True:
    jogo={'jogador1':randint(1,6),
      'jogador2':randint(1,6),
      'jogador3':randint(1,6),
      'jogador4':randint(1,6)}
    ranking=list()      
    print('Valores sorteados')
    for k,v in jogo.items():
        print(f'{k} tirou {v} no dado.')
    sleep(1)
    ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
    print('-='*50)
    print('     ==RANKING DOS JOGADORES==     ')
    for i,v in enumerate(ranking):
        print(f'{i+1}º lugar:  {v[0]} com {v[1]}.')
        sleep(1)
    rodadas=0
    for c in range(rodadas+1):
        print(f' O numero de rodadas {rodadas}')

    opcao=(input("Vamos jogar novamente? (S/N): ")).upper()
    
    if opcao=='S':
       game=True

    else:
        
        print('Obrigado por jogar!')
        break
    
print(ranking)