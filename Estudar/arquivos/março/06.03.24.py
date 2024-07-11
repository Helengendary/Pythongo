class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        
    def descricao(self):
        print(F'{self.nome}, {self.idade}, {self.raca}')
        
cao = Cachorro