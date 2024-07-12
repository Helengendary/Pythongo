# import time
# inicio = int(input('Digite o número que você quer iniciar a contagem: '))
# final = int(input('Digite o número final da contagem: '))
# passos = int(input('Quer contar de quantos em quantos? '))
# def contador(a,b,c):
#     if a > b:
#         c = -c
#     for i in range(a,(b+1),c):
#         print(i)
#         time.sleep(0.2)
# contador(1,20,1)
# contador(0,105,5)
# contador(96,52,2)
# contador(3,41,1)
# contador(75,15,5)
# contador(390,39,10)
# contador(inicio, final, passos)

import math
def operacoes(a):
    return {'Raiz Quadrada:':  math.sqrt(a), 'Quadrado:' : (a**2), 'Inverso:': 1/a, 'Fatorial:': math.factorial(a)}  
while True:
    valor = int(input('Digite um valor: '))
    resultado = operacoes(valor)   
    for j in resultado:
        print(j, resultado [j], '\n')
    saida = int(input('Digite 0 para sair digite 1 para continuar \n'))
    if saida == 0:
        break
