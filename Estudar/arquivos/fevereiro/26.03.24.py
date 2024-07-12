import argparse

parser = argparse.ArgumentParser(description='Palavras no texto')
parser.add_argument('--palavra', action='store', dest='file_palavra', required=False, help="palavra a ser achada em letra minusculas")
arguments = parser.parse_args()
palavra = arguments.file_palavra


arquivo = open('Estudar/textos/arquivo.txt', 'r')
texto = arquivo.read()

repetidas = 0
palavras = texto.strip().lower().split()
print(palavras)

for i in palavras:
    if i == palavra:
        repetidas += 1     

print(f'A palavra "{palavra}" repete {repetidas} vezes no texto.')
arquivo.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# while 1:
#     try:
#         num = int(input('Insira um numero: '))
#         break
#     except ValueError:
#         print('Insira um numero invalido')
# print('obrigado')

# lista = []
# try:
#     print(lista[8])
# except IndexError:
#     print('Erro')