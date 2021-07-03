# Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    taxa=float(taxaImposto.replace('%',''))/100
    calculo_custo=custo+(custo*taxa)
    return calculo_custo

valor=float(input('Digite o valor do imóvel: '))
multa=input('Digite o percentual do imposto: ')
resultado=somaImposto(multa,valor)
print(f'O valor com imposto é R${resultado:.2f}')    
