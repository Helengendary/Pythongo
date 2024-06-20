tamanho = 5
sequencia = [1,2,3,4,5]

arena = [""] * tamanho
for i in range(len(arena)):
    arena[i] = [0]*tamanho

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