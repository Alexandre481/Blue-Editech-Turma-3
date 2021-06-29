## Faça um programa que tenha função chamada voto() que vai receber  como parâmetro 
##  o ano de nascimento  de uma pessoa, retornando  um valor
##  literal indicando se uma pessoa  tem voto negado ,opcional  ou Obrigatório na eleições:
##   < 16 =NEGADO
##   16,18 e mais  que 70=OPCIONAL
##   As demais =Obrigatório

def voto (ano):
    atual=2021
    idade=atual-ano
    if idade < 16:
        return f'Com {idade} anos:Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f' Com  {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

print(voto(1980)) 
