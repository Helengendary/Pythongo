class Livro():
    pagina = 1
    
    def __init__(self, titulo: str, autor: str, qtd_paginas: int, guardado=True):
        self.titulo = titulo
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.guardado = guardado
        
    def pegarLivro(self):
        if self.guardado == True:
            self.guardado = False
            print('Agora você está com o livro.\n')
        else:
            print('Perdão, livro não encontrado!\n')
            
    def devolverLivro(self):
        if self.guardado == False:
            self.guardado = True
            print('Pronto, o livro já está de volta no lugar! :)\n')
        else:
            print('Opa, o livro já está aqui!\n')
            
    def virarPagina(self):
        if self.guardado == False:
            if Livro.pagina == self.qtd_paginas:
                print(f'Página: {Livro.pagina}\n')
                print('Está é a última página!\n')
            else:
                Livro.pagina += 1
                print(f'Página: {Livro.pagina}\n')
        else:
            print('Opa, você não está com o livro!\n')
    
    def virar_n_paginas(self):
        print(f'Você está na página {Livro.pagina}\n')
        quant = int(input('Quer avançar quantas páginas: '))
        if self.guardado == False:
            if quant >= self.qtd_paginas:
                print('Não dá para avançar tantas páginas!\n')   
            elif Livro.pagina >= self.qtd_paginas:
                print('O livro acabou!\n')
            else:
                Livro.pagina += quant
                print(f'Agora você está na página {Livro.pagina}\n')
        else:
            print('Opa, você não está com o livro!\n')
    
    def voltarPagina(self):
        print(f'Você está na página {Livro.pagina}\n')
        if self.guardado == False:
            if Livro.pagina <= 1:
                print('Não dá mais para voltar\n')
            else:
                Livro.pagina -= 1
                print(f'Agora você está na página {Livro.pagina}\n')
        else:
            print('Opa, você não está com o livro!\n')
    
    def voltar_n_pagina(self):
        print(f'Você está na página {Livro.pagina}\n')
        quantidade = int(input('Quer voltar quantas páginas: '))
        if self.guardado == False:
            if Livro.pagina <= 1:
                print('Não dá mais para voltar\n')
            elif quantidade > Livro.pagina:
                print('Não dá para voltar tantas páginas!')
            else:
                Livro.pagina -= 1
                print(f'Agora você está na página {Livro.pagina}\n')
        else:
            print('Opa, você não está com o livro!\n')
            
    def lerLivro(self):
        print(f'''Nome do livro: {self.titulo}
Nome do autor: {self.autor}''')
            
livro = Livro('A revolução dos bichos', 'George Orwell', 112)
livro.lerLivro()