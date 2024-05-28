import random

print('''
Um roubo de carro ocorreu dentro do campus da faculdade. 
O veículo roubado pertence a um professor renomado da instituição. 
Há suspeitas de que o ladrão tenha tido a ajuda de um cúmplice para cometer o crime. 
A investigação está em curso, e cabe aos jogadores desvendar quem são os culpados.\n''')

print('perguntas\n')

pistas = ['\nSe o carro foi roubado, então o alarme não foi acionado.\n', 
          '\nO carro foi visto pela última vez no estacionamento do bloco 3.\n', 
          '\nO cúmplice do ladrão estava na faculdade na hora do roubo.\n', 
          '\nO ladrão não possui carteirinha de estudante para entrar no campus.\n',
          '\nSe o ladrão é um estudante, então ele frequentou a aula de matemática naquele dia.\n',
          '\nSe o ladrão é um professor, então ele tem acesso ao estacionamento reservado.\n',
          '\nO cúmplice não estava no mesmo local que o ladrão durante o roubo.\n',
          '\nNa noite do roubo, houve um apagão no campus da faculdade.\n']

quantidade_dica = 0
repetidas = ''
verifica = 1
tentativas = 0

while True:
    opcao = int(input('1 -> Pedir dica\n2 -> Acertou\n3 -> Palpites\n'))
    indice = random.randint(0, 7)

    while True:
        if str(indice) in repetidas:
            indice = random.randint(0, 7)
            if len(repetidas) >= 8:
                break
        else: 
            break

    match opcao:
        case 1:
            repetidas += str(indice)
            print(pistas[indice])
            quantidade_dica += 1

            if len(repetidas) > 8:
                print('\nSuas dicas acabaram!!! Dê seu palpite!')

        case 2:
            print(f'\nParabens!\nVocê precisou de {quantidade_dica} dicas')
            break
        
        case 3:
            print('Digite qual opção está você acha que é o cúmplice e o ladrão:\n')
            cumplice = int(input("1 - Mauro da Vila Pinto e Tia da Limpeza\n2 - Estudante de Medicina e a Professora de Anatomia\n3 - Tia da Limpeza e Estudante de Medicina\n4 - Estudante de Engenharia e Mauro da Vila Pinto\n5 - Professora de Anatomia e Estudante de Engenharia"))
            if cumplice == 2:
                print(f"Acertou a resposta!\nTentativas: {tentativas}")
                break
            else: 
                tentativas +=1
                print('Errou!')