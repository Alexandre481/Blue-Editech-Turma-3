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



from random import randint
from time import sleep
from operator import itemgetter

while True:
    rodadas=int(input('Quantas rodadas você deseja jogar?:')) ##Usuário defini quantas vezes quer jogar
    print()
    vitoria=list()
    for i in range(rodadas): ###Utilização de laço for para ler as rodadas escolhidas
        valores=[randint (1,6),randint (1,6),randint (1,6),randint (1,6)]  #### Guardando os valores randomicos num dicionario.
        jogo={}
        for i in range(1,5):
            jogo[f'jogador{i}']=valores[i-1] ###Associar os jogadores em um dicionário
        ranking=list()      
        print('Valores sorteados')
        for k,v in jogo.items(): ### Associcando com o laço for jogador com pontuação
            print(f'{k} tirou {v} no dado.')
        sleep(1)
        ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
        print()
        print('     ==RANKING DOS JOGADORES==     ')
        vencedores_Rodada=list()
        for i,v in enumerate(ranking):
            if v[1] == max(valores):
                vencedores_Rodada.append(v[0])

            print(f'{i+1}º lugar:  {v[0]} com {v[1]}.')
            sleep(1)
        print()
        if len(vencedores_Rodada) > 1:
            print('Empate ninguém pontuou') 
        else:
            vitoria.append(vencedores_Rodada[0])#####Defirnir qual o campeão da rodada
    if vitoria.count('jogador2') < vitoria.count('jogador1') > vitoria.count('jogador3') and vitoria.count('jogador1') > vitoria.count('jogador4'):
       print('O grande campeão é o jogador1')
    elif  vitoria.count('jogador1') < vitoria.count('jogador2') > vitoria.count('jogador3') and vitoria.count('jogador2') > vitoria.count('jogador4'):
        print('O grande campeão é o jogador2')
    elif  vitoria.count('jogador1') < vitoria.count('jogador3') > vitoria.count('jogador2') and vitoria.count('jogador3') > vitoria.count('jogador4'):
        print('O grande campeão é o jogador3')
    elif  vitoria.count('jogador1') < vitoria.count('jogador4') > vitoria.count('jogador2') and vitoria.count('jogador4') > vitoria.count('jogador3'):
        print('O grande campeão é o jogador4')

    else: ####Alternativa para empate
        print('Empate ninguém pontou')
    opcao=(input("Vamos jogar novamente? (S/N): ")).upper()
    
    if opcao=='S':
       game=True

    else:
        
        print('Obrigado por jogar!')
        break
