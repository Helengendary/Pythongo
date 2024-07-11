# dados = open('dados.txt', 'w')
# processados = open('dados_processados.txt', 'w')
# dados.write('''mariana, 10, 9, 10
# helena, 20, 20, 1000
# adrian, 5000, 120, 25
# Juan, 04, 05, 2004
# kauane, 41, 23, 96
# milena, 70, 52, 43
# juliana, 85, 12, 75''')  

# dados = open('dados.txt', 'r')
# texto = dados.read()

# for i in texto:
#     alunos = texto.split('\n')
# maior_nota = 0

# for item in range(len(alunos)):      
#     op = alunos[item]
#     op = op.split(', ')
#     media = round((int(op[1]) + int(op[2]) + int(op[3])) / 3)   

#     if media > maior_nota:
#         maior_nota = media
#         nome = op[0]   

#     if media >= 70:
#         aprovado = 'aprovado'
#     else:
#         aprovado = 'reprovado'    

#     processados.write(op[0] + f' media: {media} - {aprovado}\n')  

# print(f'A maior nota foi de {nome} que foi: {maior_nota}')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
arquivo = open('textos/texto_exemplo.txt', 'w')
arquivo.write('''I was a liar
I gave into the fire
I know I shoulda fought it
At least Im being honest

Feel like a failure
Cause I know that I failed ya
I shoulda done you better
Cause you dont want a liar

And I know, and I know, and I know
She gives you everything
But, boy, I couldnt give it to ya
And I know, and I know, and I know
That you got everything
But I got nothing here without ya

So one last time
I need to be the one who takes you home
One more time
I promise after that, I will let you go
Baby, I dont care if you got her in your heart
All I really care is you wake up in my arms
One last time
I need to be the one who takes you home

I dont deserve it
I know I dont deserve it
But stay with me a minute
I swear I will make it worth it

Cant you forgive me?
At least just temporarily
I know that this is my fault
I should have been more careful

And I know, and I know, and I know
She gives you everything
But, boy, I couldnt give it to ya
And I know, and I know, and I know
That you got everything
But I got nothing here without you, baby

So one last time
I need to be the one who takes you home
One more time
I promise after that, I will let you go
Baby, I dont care if you got her in your heart
All I really care is you wake up in my arms
One last time
I need to be the one who takes you home

I know I shoulda fought it
At least Im being honest, yeah
But stay with me a minute
I swear I will make it worth it, yeah
Cause I dont wanna be without ya

So one last time
I need to be the one who takes you home
One more time
I promise after that, I will let you go
Baby, I dont care if you got her in your heart (babe)
All I really care if you wake up in my arms
One last time
I need to be the one who takes you home (yeah)

One last time
I need to be the one who takes you home''')


arquivo = open('textos/texto_exemplo.txt', 'r')
texto = arquivo.read()
print(texto, '\n')

for i in texto:
    palavras = texto.split()

originais = []
for i in palavras:
    if i not in originais:
        originais.append(i)
    
print(len(originais), '\n')
    
arquivo = open('textos/texto_exemplo.txt', 'w')
for i in originais:
    arquivo.write(f'{i} \n')
    
arquivo.close()