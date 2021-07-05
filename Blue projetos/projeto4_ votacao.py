# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação.
numero_voto = 0
eleito = ''
## Função para definir quem esta em condições de votar
def autoriza_voto(ano):
    from datetime import date       
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return 'Negado'
    elif 16 <= idade < 18 or idade > 65:
        return 'Opcional'
    else:
        return 'Obrigatório'

# Lista de candidatos
votacao_dict = {'candidato1':list(),
                'candidato2':list(),
                'candidato3':list(),
                'candidato1_nome':'Candidato 1',
                'candidato2_nome':'Candidato 2',
                'candidato3_nome':'Candidato 3',
                'voto_nulo':list(),
                'voto_em_branco':list()
                }
#Função para contabilizar votos
def votacao(autoriza_voto , voto):
    from datetime import date
    ano_atual = date.today().year
    if autoriza_voto == 'Obrigatório' or autoriza_voto == 'Opcional':
        if voto == 1 or voto == '1':
            votacao_dict['candidato1'].append(1)
            return 'Você votou.'
        elif voto == 2 or voto == '2':    
            votacao_dict['candidato2'].append(1)
            return 'Você votou.'
        elif voto == 3 or voto == '3':    
            votacao_dict['candidato3'].append(1)
            return 'Você votou.'
        elif voto == 4 or voto == '4':    
            votacao_dict['voto_nulo'].append(1)
            return  'Você votou nulo.'
        elif voto == 5 or voto == '5':    
            votacao_dict['voto_em_branco'].append(1)
            return 'Você votou em branco.'
        else:
            votacao_dict['voto_nulo'].append(1)
            return ' Você votou nulo'
    elif autoriza_voto == 'Negado':
        return 'Você não tem idade para votar.'  
        
        ## Contagem de votos

    elif autoriza_voto == 'mostrar' and voto == 0:
        total_votos_validos = sum(votacao_dict['candidato1']) + sum(votacao_dict['candidato2']) + sum(votacao_dict['candidato3'])
        total_votos_invalidos = sum(votacao_dict['voto_nulo']) + sum(votacao_dict['voto_em_branco'])
        if sum(votacao_dict['candidato1']) / total_votos_validos > sum(votacao_dict['candidato2']) / total_votos_validos and sum(votacao_dict['candidato1']) / total_votos_validos > sum(votacao_dict['candidato3']) / total_votos_validos:
            eleito = votacao_dict['candidato1_nome']
            numero_votos = sum(votacao_dict['candidato1'])
        elif sum(votacao_dict['candidato2']) / total_votos_validos > sum(votacao_dict['candidato1']) / total_votos_validos and sum(votacao_dict['candidato2']) / total_votos_validos > sum(votacao_dict['candidato3']) / total_votos_validos:
            eleito = votacao_dict['candidato2_nome']
            numero_votos = sum(votacao_dict['candidato2']) 
        elif sum(votacao_dict['candidato3']) / total_votos_validos > sum(votacao_dict['candidato1']) / total_votos_validos and sum(votacao_dict['candidato3']) / total_votos_validos > sum(votacao_dict['candidato2']) / total_votos_validos:      
            eleito = votacao_dict['candidato3_nome']
            numero_votos = sum(votacao_dict['candidato3'])
        

        return f'''
        Resultado da eleição do ano {ano_atual}
        {votacao_dict['candidato1_nome']}: {sum(votacao_dict['candidato1'])}
        {votacao_dict['candidato2_nome']}: {sum(votacao_dict['candidato2'])}
        {votacao_dict['candidato3_nome']}: {sum(votacao_dict['candidato3'])}
        Total de votos nulos: {sum(votacao_dict['voto_nulo'])}
        Total de votos em branco: {sum(votacao_dict['voto_em_branco'])}
        Total de votos válidos: {total_votos_validos}
        Total de votos inválidos: {total_votos_invalidos}
        O candidato eleito: {eleito} com {numero_votos} votos.
        '''
        
# Programa principal
print(f'''
            Bem vindo ao sistema de votação
            Os candidatos disponiveis são:
            [1] {votacao_dict['candidato1_nome']} 
            [2] {votacao_dict['candidato2_nome']}
            [3] {votacao_dict['candidato3_nome']}
''')
altera_nome = input('Deseja mudar os nomes dos candidatos? [S/N]: ').strip().upper()[0]
while altera_nome not in ['S','N']:
    altera_nome = input('Não entendi. Deseja mudar os nomes dos candidatos? [S/N] ').strip().upper()[0]
if altera_nome == 'S':
        votacao_dict['candidato1_nome'] = input('Informe o nome do candidato 1: ').strip().capitalize()
        votacao_dict['candidato2_nome'] = input('Informe o nome do candidato 2: ').strip().capitalize()
        votacao_dict['candidato3_nome'] = input('Informe o nome do candidato 3: ').strip().capitalize()
print("Sistema está pronto para votação.")
check_valor = True
while check_valor == True:
    print(f''' 
    [1] {votacao_dict['candidato1_nome']} 
    [2] {votacao_dict['candidato2_nome']}
    [3] {votacao_dict['candidato3_nome']} 
    [4] Voto Nulo
    [5] Voto em Branco
    ''')
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    autorizacao = autoriza_voto(ano_nasc)
    numero_candidato = int(input('Informe o numero do seu candidato: '))
    processo_voto = votacao(autorizacao, numero_candidato)
    print(processo_voto)
    check = input('Deseja fechar a votação? [S/N]: ').strip().upper()[0]
    while check not in ['S','N']:
        check = input('Deseja fechar a votação? [S/N] ').strip().upper()[0]
    if check == 'S':
        check_valor = False

print(votacao('mostrar',0))     







