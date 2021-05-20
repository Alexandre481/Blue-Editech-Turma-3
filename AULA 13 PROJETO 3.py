##AULA 13 PROJETO 3
### Adicionando valores em um dicinário
##Exemplo

###vingadores=[ nome dos vingadores:nome do personagem]
##vingadores["Michael Myers"]="555-777"
##vingadores["Gal Gadot"]="Mulher Maravilha"
##print(vingadores)

###Exercicio Aula 13 Adicionando nomes no dicionário
dicionario_vingadores={"Chris Evans":"Capitao America","Mark Ruffalo":"Hulk","Tom Hiddelston":"Loki","Chris Hemoth":"Thor","Robert Downey Junior":"Homem de ferro","Scarlet Johanson":"Viuva Negra" }
##dicionario_vingadores["Gal Gadot"]="Mulher Maravilha"
##dicionario_vingadores["Tom Cruise"]="Rambo"
##print(dicionario_vingadores)


##Excluindo valores dicionário
###del dicionario_vingadores["Tom Hiddelston"]
##print(dicionario_vingadores)

## Outra forma de excluir com retorno de valor deletado ou ator não encontrado
##print(dicionario_vingadores.pop("Chris Hemoth","Ator não encontrado"))

###dicionario_vingadores.popitem() ###exclui o ultimo item 
##print(dicionario_vingadores)


###print(dicionario_vingadores)

#### Para unir dois dicionários:
dicionario_animais_e_suas_raças={"Cachorro":"Vira lata Caramelo","Cavalo":"Mangalarga","Gato":"Siames"}
##for elementos in dicionario_animais_e_suas_raças:
   #### print(elementos)
    ##dicionario_vingadores[elementos]=dicionario_animais_e_suas_raças[elementos]
    ##print(dicionario_vingadores)

### União de dicionarios de maneira mais simples
dicionario_vingadores.update(dicionario_animais_e_suas_raças)
print(dicionario_vingadores)
   




