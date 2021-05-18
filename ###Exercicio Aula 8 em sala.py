###Exercicio Aula 8 em sala###
####	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:##
###a.	tamanho da lista.
#a.	tamanho da lista.
###	maior valor da lista.
###	menor valor da lista.
###	soma de todos os elementos da lista.
###	lista em ordem crescente.
###	lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]
print("Lista = ",L)
print("O tamanho da lista é ",len(L))
print("O maior elemento da lista é ",max(L))
print("O menor elemento da lista é ",min(L))
print("A soma dos elementos da lista é ",sum(L))
L.sort()
print("Lista em ordem crescente:",L)

L.reverse()
print("Lista em ordem decrescente: ",L)
