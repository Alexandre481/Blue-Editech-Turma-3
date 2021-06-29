# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado
aluno=(input(("Digite o nome do aluno: ")))
nota=float(input(("Digite a média do aluno: ")))
# aluno=dict()
# nota=dict()
if nota >= 7:
    print("Aluno esta aprovado")
if nota == 6.9 or 5:
 print("O aluno esta em recuperação")
if nota < 5:
  print ("O aluno est reprovado.")