# Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos.
def soma(n1, n2, n3):
    resultado=n1+n2+n3
    return resultado

nota1=float(input('Digite nota aluno 1: '))
nota2=float(input('Digite nota aluno 2: '))
nota3=float(input('Digite nota aluno 3: '))
calculo=soma(nota1, nota2, nota3)###soma é o nome da função utilizada
print(calculo)


