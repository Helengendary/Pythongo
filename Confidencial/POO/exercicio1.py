

class Alunos:
    def __init__(self, nome, idade, turma, planta) :
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.planta = planta
        
    def descricao(self):
        return f'''Nome: {self.nome}
Idade: {self.idade}
Turma: {self.turma}
Planta: {self.planta}\n\n'''

    @staticmethod
    def adiconarTexto(texto):
        arquivo = open("Avaliação Python/avaliação poo/alunos.txt", "w", encoding="utf-8") 
        arquivo.write(texto) 


nome_aluno = input("Digite o nome do aluno: ") 
idade_aluno = input("Digite a idade do aluno: ")
turma_aluno = input("Digite a turma do aluno: ")
planta_aluno = input("Digite a planta do aluno: ")
    
alunos = Alunos(nome_aluno, idade_aluno, turma_aluno, planta_aluno)
dados = alunos.descricao()
Alunos.adiconarTexto(dados)