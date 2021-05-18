###lista_contatos=[("João","123-456"),("Fabricio","456-7789"),("Samara","987-6541"),("Silvio",999.334),("Amanda",3445,668)]
###print (len(lista_contatos))
###print (lista_contatos)
###print (lista_contatos[0])
###print (lista_contatos[0][0])

####
##Exemplo de dicionário###
##contatos={"Pedro":"555-66678"}### dic={chave:valor}
###print(contatos)
##print(type(contatos))
##print(len(contatos))


####Cria um dicionário###
##variavel=dict(contatos)
##print(contatos)

###Criando um Dicionário na mão###
from typing import Type, overload


###dicionario_contatos={"Alexandre":"567895","Talita":"87879-8686","Emerson":"5556-7774"}
###print(dicionario_contatos)
##print(dicionario_contatos.get("Silvio","Nome não encontrado"))#

##Exercicio
###dicionario_vingadores={"Chris Evans":"Capitao America","Mark Ruffalo":"Hulk","Tom Hiddelston":"Loki","Chris Hemoth":"Thor","Robert Downey Junior":"Homem de ferro","Scarlet Johanson":"Viuva Negra" }
###nome=input("Digite o nome do ator ")

###print(dicionario_vingadores.get(nome,"nome não encontrado"))


###Forma COM While
###While nome not in dicionario_contatos:
###print("nome não encontrado,tente novamente")