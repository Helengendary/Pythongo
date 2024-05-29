import random 
import os
import time     

acerto = True
jogadas = 0
sorteados = []
decimal = 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
while acerto:
    jogadas += 1
    atual = random.randint(1,4)
    sorteados.append(atual)
    for i in range(jogadas):
        limpar_tela()
        print(f'{i+1}: {sorteados[i]}')
        time.sleep(1)
        limpar_tela()

    for i in range(jogadas):
        user = int(input(f"Insira o numero {i+1} da sequencia: "))
        if sorteados[i] != user:
            print("\nVocê errou")
            print(f"A sequencia era {sorteados}")
            acerto = False

    if jogadas == 100:
        print("Parabens você chegou em 100 jogadas!")
        acerto = False  

        