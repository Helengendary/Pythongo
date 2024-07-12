class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 
        self.genero = genero

    def descricao(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nGenero: {self.genero}\n\n'
    
    @staticmethod
    def imprimir(texto):
        arquivo = open('Estudar/exercicios/livros.txt', 'a')
        arquivo.write(texto)

titulo = input("Titulo: ")        
autor = input("Autor: ")        
ano = int(input("Ano: "))        
genero = input("Genero: ") 

livro = Livro(titulo, autor, ano, genero)
info = livro.descricao()
Livro.imprimir(info)