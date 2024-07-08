classe = ['1_palmeiras', '1_corintians', '2_coritiba', '1_cuiaba', '3_juventude', '2_fluminense', '3_bahia', '2_cascavel', '3_ponte preta', '2_parana clube', '3_volta redonda']

primeira = []
segunda = []
terceira = []

primeiraCorreto = []
segundaCorreto = []
terceiraCorreto = []

for i in range(len(classe)):
    if classe[i].startswith('1') == True:
        primeira.append(classe[i])
        
    elif classe[i].startswith('2') == True:
        segunda.append(classe[i])
        
    elif classe[i].startswith('3') == True:
        terceira.append(classe[i])
      
for h in range(len(primeira)):
    teste = primeira[h]
    abrev = str(teste[2:])
    abrev = abrev.capitalize()
    primeiraCorreto.append(abrev)
    
for h in range(len(segunda)):
    teste = segunda[h]
    abrev = str(teste[2:])
    abrev = abrev.capitalize()
    segundaCorreto.append(abrev)
    
for h in range(len(terceira)):
    teste = terceira[h]
    abrev = str(teste[2:])
    abrev = abrev.capitalize()
    terceiraCorreto.append(abrev)
        
print(f'Primeira divisão: {primeiraCorreto}')
print(f'Segunda divisão: {segundaCorreto}')
print(f'Terceira divisão: {terceiraCorreto}')

