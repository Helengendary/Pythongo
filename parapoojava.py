from random import randint


def aleatorio(tam):
    lista = []
    for tam in range(tam):
        lista.append(randint(1,99))
        
    return lista
    
tam = int(input("Digite o tamanho: "))
print()

sort = aleatorio(tam)

for i in range(len(sort)):
    vez = sort[i]
    
    if (vez%2) == 0:
        print(f"{vez} - Número par")
    elif (vez%3) == 0:
        print(f"{vez} - Múltiplo de três")
    else:
        print(f"{vez} - Número ímpar")
        