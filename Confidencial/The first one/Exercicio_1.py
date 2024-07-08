arquivo = open('Avaliação python/clientes.txt', 'w')
arquivo.write('''M#aria J@ose
G#abriela #Maria
Jessica lim%a**
emanuelle gar&*cia
Fab12ian#a G_+ome-s
Lucas Silveira
Adri3$ana A'!lmeida
Q+UENTI)N ?TARAN@TINO
BA+T M*AN
CLA$Rk @Kent
Bruc?e Al()ves
HELEn+a R_omulo
Nicholas!@ B#ueno
No$ah B&arbosa
Daniel? G_+onçalVES
ELBA! RAMALHO
Le*_onard#o +(Gabriel
Gabri#el Penkal?
''')

arquivo = open('Avaliação python/clientes.txt', 'r')
texto = arquivo.read()

for i in texto:
    nomes = texto.strip().split('\n')

# correto = []
# j=0
# l=0

# for h in nomes:
#     nome = nomes[j]
#     j+=1
#     for l in nome:
#         nome = nome[l]
#         l+=1
#         if nome.isalpha() == True:
#             correto.append(nome)

# print(correto)