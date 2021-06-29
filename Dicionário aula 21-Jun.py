#   Crie um programa que leia nome, ano de nascimento e 
#   carteira de trabalho e cadastre-os (com idade) em um dicionário.
#    Se por acaso a CTPS for diferente de 0, o dicionário
#     receberá também o ano de contratação e o salário. Calcule e acrescente , 
#     , com quantos anos a pessoa vai se aposentar. 
#     Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
dados=dict()
dados['nome']=str(input('Nome:  '))
nasc=int(input('Ano de nascimento:'))
dados['idade']=2021-nasc
dados['ctps']=int(input('Carteira de trabalho (0 não tem):'))
if dados ['ctps'] !=0:
    dados['contratação']= int(input('Ano de contratação: '))
    dados['salário']=float(input('salário: R$'))
    dados['aposentadoria']=dados['idade']+((dados['contratação']+ 35 )-2021 )
print('-='*30)
print(dados)