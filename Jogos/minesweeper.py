import random

tamanho = 5 # tamanho temporário da arena
quantidadeBombas = 5 # quantidade de bombas da arena

sequencia = [] # Para imprimir as coordenadas
for i in range(tamanho):
    sequencia.append(i+1)

xs = [] # todos os x (colunas) que tem bomba
ys = [] # todos os y (linhas) que tem bomba
totalBombas = 0 # quantidade de bombas já adicionadas na arena

# Fazer arena
arena = [""] * tamanho
for i in range(len(arena)):
    arena[i] = [" "] * tamanho

# Função para printar arena
def Arena():
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

userX = int(input('Digite o x: '))
xs.append(userX)
userY = int(input('Digite o y: '))
ys.append(userY)

# Condiçoões para colocar as bombas
while(totalBombas < quantidadeBombas):
    faz = True
    y = random.randint(0, 4)
    x = random.randint(0, 4)
    for f in range(len(xs)):
        if x == xs[f] and y == ys[f]:
            faz = False

    if faz:
        arena[x][y] = "▣" 
        print(f'x {x}\ty: {y}')
        xs.append(x)      
        ys.append(y)  
        totalBombas+=1

print(totalBombas)

# Funções das coordenadas de identificação das bombas
presencaBombas = 0

def EsquerdoCima(i, j):
    if arena[i-1][j-1] == "▣":
        global presencaBombas
        presencaBombas+=1

def Esquerdo(i, j):
    if arena[i][j-1] == "▣":
        global presencaBombas
        presencaBombas+=1

def EsquerdoBaixo(i, j):
    if arena[i+1][j-1] == "▣":
        global presencaBombas
        presencaBombas+=1

def MeioCima(i, j):
    if arena[i-1][j] == "▣":
        global presencaBombas
        presencaBombas+=1

def MeioBaixo(i, j):
    if arena[i+1][j] == "▣":
        global presencaBombas
        presencaBombas+=1

def DireitoCima(i, j):
    if arena[i-1][j+1] == "▣":
        global presencaBombas
        presencaBombas+=1
        
def Direito(i, j):
    if arena[i][j+1] == "▣":
        global presencaBombas
        presencaBombas+=1

def DireitoBaixo(i, j):
    if arena[i+1][j+1] == "▣":
        global presencaBombas
        presencaBombas+=1

# Verifições das bombas ao redor
for i in range (tamanho):
    for j in range(tamanho):
        presencaBombas = 0
        if arena[i][j] == "▣":
            continue
        else:
            if i == 0:
                MeioBaixo(i, j)
                if j == 0:
                    Direito(i, j)
                    DireitoBaixo(i, j)
                elif j == tamanho-1:
                    Esquerdo(i, j)
                    EsquerdoBaixo(i, j)
                else:
                    Direito(i, j)
                    DireitoBaixo(i, j)
                    Esquerdo(i, j)
                    EsquerdoBaixo(i, j)

            elif i == tamanho-1:
                MeioCima(i, j)
                if j == 0:
                    Direito(i, j)
                    DireitoCima(i, j)
                elif j == tamanho-1:
                    Esquerdo(i, j)
                    EsquerdoCima(i, j)
                else:
                    Direito(i, j)
                    DireitoCima(i, j)
                    Esquerdo(i, j)
                    EsquerdoCima(i, j)

            elif j == 0:
                if i != 0 and i != tamanho-1:
                    Direito(i, j)
                    DireitoBaixo(i, j)
                    DireitoCima(i, j)
                    MeioBaixo(i, j)
                    MeioCima(i, j)

            elif j == tamanho-1:
                if i != 0 and i != tamanho-1:
                    MeioBaixo(i, j)
                    MeioCima(i, j)
                    Esquerdo(i, j)
                    EsquerdoBaixo(i, j)
                    EsquerdoCima(i, j)
            else:
                Direito(i, j)
                DireitoBaixo(i, j)
                DireitoCima(i, j)
                Esquerdo(i, j)
                EsquerdoBaixo(i, j)
                EsquerdoCima(i, j)
                MeioBaixo(i, j)
                MeioCima(i, j)
                
            arena[i][j] = presencaBombas


suprema = Arena()

# Print das coordenadas das bombas
print()
print(xs)
print(ys)