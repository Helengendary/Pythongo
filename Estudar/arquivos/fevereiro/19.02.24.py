#lista = [7, 4, 2, 0, 6]
# lista.sort() #coloca em ordem crescente
# print(lista)
# lista = ['g', 'y', 'h']
# lista.sort() #coloca em ordem crescente
# lista[0] = 'a'
# print(lista)

#jogo = [7, 3, 4, 9, 1]
# print(1 in jogo)
# print(8 in jogo)

# print(jogo + lista)
# print(jogo * 2 + lista * 4)
# print((jogo * 2) + (lista * 4))

# print(min(jogo))
# print(sum(lista))

# lista = [0,0,0,0,0,0,0,0,0,0]
# lista[0] = int(input('VALOR 1: '))
# lista[1] = int(input('VALOR 2: '))
# lista[2] = int(input('VALOR 3: '))
# lista[3] = int(input('VALOR 4: '))
# lista[4] = int(input('VALOR 5: '))
# lista[5] = int(input('VALOR 6: '))
# lista[6] = int(input('VALOR 7: ')) 
# lista[7] = int(input('VALOR 8: '))
# lista[8] = int(input('VALOR 9: '))
# lista[9] = int(input('VALOR 10: '))
# tamanho = len(lista)
# lista.sort()
# print('Tamanho da lista: ', tamanho )
# print(lista)


#ricos = ('Jeff Bezos', 'Bill Gates', 'Warren Buffet', 'Bernard Arnault', 'Amâncio Ortega', 'Larry Ellison', 'Mark Zuckerberg', 'Miche. Booberg', 'Larry Page')
# print('Os 10 mais ricos do mundo em 2019 são:', ricos)
# print('Os 3 mais ricos do mundo em 2019 são: ', ricos[:3])
# print('O mais rico do mundo em 2019 é: ', ricos[0])

# print('Menu FastFood')
# valores = {'hamburger':10, 'hotdog' : 6.5, 'salada':4, 'suco':4, 'refrigerante':4.5, 'agua':2}
# print(valores)
# comida = input('Digite a comida que você deseja: ')
# bebida = input('Digite o bebida que você deseja: ')
# total = valores[comida] + valores[bebida]
# print('O valor total ficou de: ', total)

# segredo = '12'
# palpite = input('Digite seu palpite: ')
# if not palpite.isdigit():
#     print('Número inválido')
# if palpite == segredo:
#     print('ACERTOU!!')
# else:
#     if palpite.isdigit():
#         print('ERROU!!')



# ano = int(input('Qual ano você nasceu?'))
# print(ano)
# idade = int(2024 - ano)
# if idade < 16 and idade > 70:
#     print('Seu voto é facultativo!')
# elif idade >=18 and idade <=70:
#         print('Seu voto é obrigatório!')
# elif idade < 16:
#     print('Você não pode votar!')



# limite = int(input('Digite qual o limite: '))
# soma = 0
# i = 1
# while i <= limite:
#     soma = i + soma
#     i += 1   
# print('O valor total da soma é ', soma) 


primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo número: '))
while True:
    conta = int(input('Digite:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n'))
    if conta == 0: 
        break
    elif conta == 1:
        print('A soma dos números é ', primeiro_numero + segundo_numero)
    elif conta == 2:
        print('A subtração dos números é ', primeiro_numero - segundo_numero)
    elif conta == 3:
        print('A multiplicação dos números é ', primeiro_numero * segundo_numero)
    elif conta == 4:
        print('A divisão dos números é ', primeiro_numero / segundo_numero)
    saida = int(input('Se Deseja sair digite 0, se não digite qualquer valor\n'))
    if saida == 0:
        break