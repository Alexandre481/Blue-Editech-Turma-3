# for c in range(0,3):
#     numero = int(input('Digite um numero:'))
#     total_num = c+1 + numero+1
# print(total_num)
# from time import  sleep
# cont = 10
# while cont != 0:
#     print(cont)
#     cont -=1
#     sleep(1)
# print('Feliz ano novo!!!')

L = [4, 2, 1, 7]
a = L[0]
for e in L:
    if e < a:
        a = e
print(a)