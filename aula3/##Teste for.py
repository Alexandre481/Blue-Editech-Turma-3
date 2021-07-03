##Teste for
frase=input("Digite uma frase:").lower()
vogais=""

for  letra in frase:
    
    if not letra in 'aeiou':
     vogais +=letra
print(f' A frase:{frase}, possui {vogais} vogais')
    