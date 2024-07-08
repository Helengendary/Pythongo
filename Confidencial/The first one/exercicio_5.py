#cria uma lista
lista = []   

#a variável "tam" pede para o usuário inserir o tamanho que ele quer que a lista seja
tam=int(input("Digite o tamanho da lista: "))

#esse primeiro "for" repete com base no tamanho que o usuário digitou e para adicionar os valores que o usuário quer adicionar na lista 
#o primeiro valor dentro do "range" é para indicar qual número começa a contar a repetição, o segundo valor é onde termina, e o terceiro era para que conte de um em um
for i in range (1, tam+1, 1):
    x=int(input("VALOR {} : ".format(i)))
    lista.append(x)
    
#esses dois "print" imprimem para o usuário ver como a lista dele ficou
print("\nLISTA:")
print(lista)

#todo esse bloco serve para colocar os números em ordem crescente
#esse "for" faz a contagem de qual número vai ser comparado com os outros
for i in range(tam):
    #esse "for" compara o "i" com os outros da lista 
    for j in range(tam):
        #esse if faz com que caso o item "j" for maior que o item "i" eles troquem de lugar
        if lista[j] > lista [i]:
            lista[i],lista[j]=lista[j],lista[i]

#esses dois "print" imprimem para o usuário a lista em ordem crescente
print("\nLISTA ORDENADA: ")
print(lista)