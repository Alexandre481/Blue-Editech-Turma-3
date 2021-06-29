 ###Crie um programa onde o usuário possa digitar vários valores numéricos e
####cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
###adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
####crescente.
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        condicao = str(input('Deseja continuar? S ou N? ')).upper()
        if condicao == 'S' or condicao == 'N': break
        print('Essa opção não existe. Tente de novo.')
    if condicao == 'N': break
numeros.sort()
unicos = list(set(numeros))
#O comando  list(set(lista))  faz com que os números repetidos digitados não se repitam.
print(f'Os números digitados (excluindo os duplicados) foram {unicos}')