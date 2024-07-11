import random
import colorama 
from colorama import Fore, Style
colorama.init()

op = ['Scissor', 'Paper', 'Rock']

while True:
    user = int(input(Fore.WHITE +  '''
                     
    Choice: 
    1 -> Scissor
    2 -> Paper
    3 -> Rock
    4 -> Sair

    R: '''))

    if user == 4:
        break
    
    user -= 1

    comp = random.randint(0,2)

    print(Fore.WHITE + f'''
    You: {op[user]}
    Machine: {op[comp]}
    ''')

    if user == comp:
        print(Fore.YELLOW + 'It´s a draw!!! ¯\_(ツ)_/¯')
    elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
        print(Fore.GREEN + 'The user WON!! (❤´艸｀❤)')
    else:
        print(Fore.RED + 'The computer WON!! o(〃＾▽＾〃)o')

print(Fore.WHITE + 'Thank you for playing! (★‿★)')