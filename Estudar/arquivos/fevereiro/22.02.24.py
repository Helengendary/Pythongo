# import random
# numeros = []
# i = 0
# inferior = int(input('Digite o limite inferior: '))
# Superior = int(input('Digite o limite superior: '))
# tamanho = int(input('Digite o tamanho da lista: '))
# while i < tamanho:
#     numeros.append(random.randint(inferior, Superior))
#     i += 1   
# print(numeros)
# for a in range(tamanho):
#     for h in range(tamanho):
#         if numeros[a] < numeros[h]:
#             ux = numeros[a]
#             numeros[a] = numeros[h]
#             numeros[h] = ux
# print(f'LISTA ORDENADA: {numeros}')            




# arquivo = open('arquivo.txt', 'w')
# arquivo.write('yes, and?')
# arquivo.close()

# arquivo = open('arquivo.txt', 'r')
# print(arquivo.read())
# arquivo.close()




arquivo = open('Estudar/textos/arquivo.txt', 'r')
texto = arquivo.read()
print(texto)
user = input('Escolha uma palavre e eu te direi quantas vezes aparece no texto ')
repetidas = 0
palavra = texto.strip().lower().split()
# print(palavra)
for i in palavra:
    if ',' in i:
        au=0
        l=''
        for j in i:
            if not (j in ','):
                l+=j
                au+=1
        i = l
    if user == i:
        repetidas+=1     
print(f'A palavra "{user}" repete {repetidas} vezes no texto.')
arquivo.close()