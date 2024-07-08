while True:
    try:
        user = int(input("Insira um número maior que zero\n"))
        if user > 0:
            break
        else:
            print('Número inválido. Tente novamente!')
    except ValueError:
        print('Insira um número!')

user = str(user)

j = 0
contador = 0

for i in user:
    nmr = user[j]
    nmr = int(nmr)
    soma = nmr + contador
    contador = soma
    j += 1
    
print(f'A soma dos algarismos é igual a {soma}')