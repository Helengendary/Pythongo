# lista = ('a','b','c','d','e','f','g','h')
# for i in range (2,10,2): #primeiro número é o start, segundo a quantidade de números, terceiro quantos passos
#     print(i)


# for i in range(0,31):
#     if i%2 == 0:
#         print(i)


# tabuleiro = int(input('Digite um número inteiro para o tabuleiro: '))
# for h in range (tabuleiro):
#     for i in range (tabuleiro):
#         print('X', end = ' ')
#     print('')



fib = 0
onacci = 1
num = int(input('Digite a quantidade de fatores para a série de Fibonacci: '))
for i in range (num):
    fibonacci = fib + onacci
    fib = onacci
    onacci = fibonacci
    print(fib)


# primo = int(input('Digite um número: '))
# nums = []
# for i in range(1,primo+1,1):
#     if primo % i == 0: 
#         nums.append(i)        
# if len(nums) > 2:
#     print(nums)
#     print('NÃO É PRIMO')
# else:
#     print(nums)
#     print('PRIMO')


# import random
# vitorias = 0
# while True:
#     user = int(input('Digite um número: '))
#     escolha = input('PAR ou IMPAR ')
    
#     comp = random.randint(1,100)
#     num = comp + user
#     print(f'O coputador jogou: {comp}')
#     print(f"RESULTADO: {num}\n")
    
#     if escolha == 'par' and num%2 == 0:
#         print('Você ganhou!')
#         vitorias += 1
#     elif escolha == 'impar' and not num%2 == 0:
#        print('Você ganhou!')
#     else:
#         print(f'Você perdeu!\nVITORIAS: {vitorias}')
#         break

# import time
# def soma(a, b):
#     total = a + b
#     print(total)

# def contagem():
#     for i in range(3,0,-1):
#         print(i)
#         time.sleep(1)
        