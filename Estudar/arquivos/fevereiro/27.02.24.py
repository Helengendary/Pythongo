# while True:
#     try:
#         primeiro_numero = int(input('\nDigite o primeiro numero: '))
#         segundo_numero = int(input('Digite o segundo número: '))
        
#         while True:
#             conta = int(input('\nDigite:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n'))
#             if conta == 0: 
#                 break
#             elif conta == 1:
#                 print('\nA soma dos números é ', primeiro_numero + segundo_numero, '\n')
#                 break
#             elif conta == 2:
#                 print('\nA subtração dos números é ', primeiro_numero - segundo_numero, '\n')
#                 break
#             elif conta == 3:
#                 print('\nA multiplicação dos números é ', primeiro_numero * segundo_numero, '\n')
#                 break
#             elif conta == 4:
#                 print('\nA divisão dos números é ', primeiro_numero / segundo_numero, '\n')
#                 break
#             else:
#                 print('\nDigite um número válido!')
        
#         if conta == 0: 
#                 break
            
#         saida = input('Se Deseja sair digite 0, se não digite qualquer valor\n')
#         if saida == 0:
#             break
#     except ValueError:
#         print('Valor inválido!\n')
#     except ZeroDivisionError:
#         print('Não é possível dividir um número por zero!\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random
from random import sample

print('''INSTRUÇÕES:
- Primeiro você deverá escolher a dificuldade: fácil (palavra de 4 letras), Médio (palavra de 5 letras), Difícil (palavra de 6 letras);
- Quando você colocar a sugestão e acertar a posição das letras aparecerá qual você acertou, senão, as que você errou aparecerá um "X";
- Você inicia com 100 pontos. E a cada letra errada você perde 10 pontos;
- OBS: Algumas palavras com acento vão aparecer sem, então, na hora de dar seu palpite não esqueça das pavras com acento ou ç (dê seu palpite sem acento)\n''')


def embaralha(nome):
    a = sample(nome,len(nome))
    d = ''.join(a)
    print(f'Adivinhe qual é essa palavra: {d}')
    

arquivo = open('textos/anagrama.txt', 'w')
arquivo.write('''CASA, BOLA, PENA, SAPO, FOCA, VIDA, JOIA, FATO, DADO, MALA, FOGO, LUPA, RIMA, VASO, ZONA, PATO, GATO, JOGO, FRIO, LIXO

Cobra, Livro, Barco, Sabio, Chuva, Limao, Regua, otimo, Jovem, Noite, Pomba, Furia, Roupa, Selva, Canto, Usado, Viola, Vacuo, Zebra, acido

Bicudo, Caneta, Dadiva, Elixir, Grampo, Helice, intimo, Janela, arvore, Madura, Nectar, orbita, Abraco, Quarto, Xadrez, Tunica, ultimo, Bebado, Canudo, queijo, Tapete''')

arquivo = open('textos/anagrama.txt', 'r')
palavras = arquivo.read()

texto = palavras.split('\n\n')

facil = texto[0]
facil = facil.split(', ')
medio = texto[1]
medio = medio.upper()
medio = medio.split(', ')
dificil = texto[2]
dificil = dificil.upper()
dificil = dificil.split(', ')

while True:
    pontos = 100
    while True:
        try:
            nivel = int(input('Qual nível você deseja ser seu jogo?\n1 - Fácil\n2 - Médio\n3 - Difícil\n'))
            
            if nivel == 1:
                plvr = random.choice(facil)
                embaralha(plvr)
                break
            elif nivel == 2:
                plvr = random.choice(medio)
                embaralha(plvr)
                break
            elif nivel == 3:
                plvr = random.choice(dificil)
                embaralha(plvr)
                break
            else:
                print('Digite um número válido!')
        except ValueError:
            print('Insira um número válido!')
            

            
    while True:
        resposta = input()
        resposta = resposta.upper()    
        palpites = []

        if resposta == plvr:
            print(f'''Parabéns você acertou a palavra era: {plvr} 
    Pontos: {pontos}''')
            break
        else:
            for i in range(len(plvr)):
                if resposta[i] == plvr[i]:
                    palpites.append(plvr[i])
                    pontos -= 10
                else:
                    palpites.append('x')
            print(palpites)
        if pontos == 0:
            print(f'Você perdeu! Está com {pontos}')
            break

    try:
        saida = int(input('''Quer continuar? 
    Digite 0 para sim e qualquer dígito entre 1 e 9 para parar\n\n'''))
        if saida != 0:
            break
    except ValueError:
        print('Digite um número!')

arquivo.close()