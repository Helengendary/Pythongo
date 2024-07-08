# o que são Classes em POO?

#     Usamos classes para criar objetos que podem ser físicos ou abstratos, e recebem métodos e atributos. 
#     Por exemplo, cachorro seria nosso objeto, então, temos uma classe com o nome cachorro, e ela vai receber métodos que são responsáveis pelas ações do cachorro, por exemplo, teria
# uma função (método) chamada latir. 
#   Mas, todo cachorro tem sua característica, como cor, raça, tamanho e nome, e isso são os atributos. Então, para criarmos o objeto precisamos de um método inicial que recebe como parâmetro as características.

class Cachorro:
    # método inicial
    def __init__(self, nome, cor, raca, tamanho):
        # atributos
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.tamanho = tamanho
        
    def descricao(self):
        print(f'''Nome: {self.nome}
Raça: {self.raca}
Cor: {self.cor}
Tamanho: {self.tamanho}\n''')
        
    @staticmethod
    def latir():
        return 'Au Au'
    
# criando o objeto 
cachorro1 = Cachorro('Picolé', 'Marrom', 'Pinscher', 'Pequeno')
cachorro1.descricao()
print(Cachorro.latir())