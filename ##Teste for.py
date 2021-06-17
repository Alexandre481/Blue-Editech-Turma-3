##Teste for
frase=input("Digite uma frase:").lower()
vogais=0

for letra in frase:
    print(letra,end=' ')
    if letra in 'aeiou':
     vogais +=1
print(f' A frase:{frase}, possui {vogais} vogais')
    