
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.
from time import sleep
import random
print("\n")
print("    ******           Bem vindo ao jogo Jokempô        ****** \n")

#variáveis para uso dentro loop while que segue abaixo
game=True                                       
jog=['papel','tesoura','pedra']                 
res=['empate','você venceu','Python venceu']    
res_cont=[0,0,0]

while game==True:         #loop enquanto jogador quiser jogar

    #Jogada do usuário
    print('''Faça sua jogada: 
    1 para Papel 
    2 para Tesoura 
    3 para Pedra''')
    jog_user=int(input("Escolha a sua opção: "))
    if jog_user<=0 or jog_user>=4:     
        print('Você digitou um número inválido')
        continue

    #Jogada do Python
    sleep(2)
    jog_cpu=random.randint(1,3)

    #Avalia quem ganhou    
    if jog_user==jog_cpu:
        Resultado=0                     #empate
    elif (jog_user==1 and jog_cpu==3) or (jog_user==2 and jog_cpu==1) or (jog_user==3 and jog_cpu==2):  
        Resultado=1                     #usuário vence
    else:
        Resultado=2         #outras opções só podem ser vitória do Python
    print('Você jogou '+jog[jog_user-1]+', Python jogou '+jog[jog_cpu-1]+', Resultado: '+res[Resultado] )

    #Soma os resultados das várias iterações do loop e apresenta resultado
    sleep(2)
    res_cont[Resultado]=res_cont[Resultado]+1
    print('Tivemos até agora '+str(res_cont[0])+' empates, '+str(res_cont[1])+' vitórias suas e '+str(res_cont[2])+' vitórias de Python')

#Pergunta ao usuário se quer permanecer no jogo ou sair, com a lógica de

    sleep(2)
    opcao=(input("Vamos jogar novamente? (S/N): ")).upper()
    
    if opcao=='N':
        game=False
    elif opcao=='S':
        game=True
    else:
        print('Resposta inválida, digitou '+opcao)
        break

print('Obrigado por jogar!')