class Empresa:
    
    def __init__(self, nome, cnpj, nacionalidade, responsavel, paises = [], produtos =[]):
        self.nome = nome
        self.__cnpj = cnpj
        self.nacionalidade = nacionalidade
        self.__responsavel = responsavel
        self.__paises = paises
        self.produtos = produtos
        self.produtos = []
        print(f'Empresa: {self.nome}\n')
        
    def getPresidente(self):
        return self.__responsavel
    
    def getPaises(self):
        return self.__paises
    
    def pais(self, pais):
        for i in self.__paises:
            if i == pais:
                print('Estamos atuando nesse país!\n')
        
    def relatorioProd(self):
        return self.produtos
    
    def addProdutos(self, produto, preco, descricao):
        self.produtos.append(f'{produto} : {preco}, {descricao}')
    
class Area(Empresa):
    def __init__(self, nome, sigla, funcao, responsavel, lucro, inicio, fim):
        self.nome = nome
        self.sigla = sigla
        self.funcao = funcao
        self.responsavel = responsavel
        self.__lucro = lucro
        self.inicio = inicio
        self.fim = fim
        print(f'Setor: {self.nome}\n')
        
    def diretor(self):
        return self.responsavel
    
    def resltorioFinan(self):
        return self.__lucro
    
    def perido(self):
        print(f'Data de Início de Auditoria: {self.inicio}\n')
        if self.fim == None:
            print('Está sendo auditada.')
        else:
            print(f'Data de Fim de Auditoria: {self.fim}\n')
        print(f'Responsável: {self.responsavel}\n')
        
class Departamento(Area):  
    def __init__(self, nome, sigla, funcao, responsavel, funcionarios):
        self.nome = nome
        self.sigla = sigla
        self.funcao = funcao
        self.responsavel = responsavel
        self.funcionarios = funcionarios
        print(f'Subsetor: {self.nome}\n')
        
    def getResponsavel(self):
        return self.responsavel
    
    def contratar(self, quant):
        self.funcionarios += quant
        
    def treinamento(self):
        print(f'Realizando treinamento com os funcionários sobre o Subsetor {self.sigla} ({self.nome})')
        
