### Exercicio 4 aula 8
##   4.Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco),
## conte quantas vezes aparece uma vogal.##
def conta_vogal(frase):
    vogais = 0
    for letra in frase:
        if letra.upper() in "AEIOU":
            vogais += 1
                        
    return vogais 

        

