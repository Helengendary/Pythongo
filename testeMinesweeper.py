import random


tamanho = 5 # tamanho temporário da arena
quantidadeBombas = 5 # quantidade de bombas da arena
sequencia = [1,2,3,4,5] # Para imprimir bunito (transformar em um for)
xs = [] # todos os x (colunas) que tem bomba
ys = [] # todos os y (linhas) que tem bomba
totalBombas = 0 # quantidade de bombas já adicionadas na arena

# Fazer arena
arena = [""] * tamanho
for i in range(len(arena)):
    arena[i] = [" "] * tamanho

helenis = 0
def zero():
    if arena[0][0] == " ":
        global helenis 
        helenis +=1


zero()

print(helenis)

for i in range (tamanho):
    if i == 0:
        print("   ", end="")
        for h in range(len(sequencia)):
            print(f" {sequencia[h]} ", end="")
        print()
    print(sequencia[i], ' ', end="")
    for j in range(tamanho):
        print(f"[{arena[i][j]}]", end="")
    print()