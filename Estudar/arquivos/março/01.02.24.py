# class Casa:
#     def __init__(self, area, cor, rua):
#         self._area = area
#         self._cor = cor
#         self._rua = rua
#         self.luz = False
#         self.energia = False
#         print('objeto criado\n')
        
#     def __del__(self):
#         pass
        
#     def __del__(self):
#         pass
    
#     def ligar_luzes (self):
#         if self.energia == True:
#             self.luz = True
            
#     def  desligar_luzes (self):
#         self.luz == False

#     @staticmethod
#     def cortarEnergia ():
#         Casa.energia = False
        
#     @staticmethod
#     def ligarEnergia ():
#         Casa.energia = True
        
# Casa.ligarEnergia()

# print('Criando casa do João')
# casaJoao = Casa(120, 'azul', 'avenida salgado filho')

# print(f'Cor: {casaJoao._cor}, Rua: {casaJoao._rua}, Área: {casaJoao._area}\n')

#----------------------------------------------------------------------------------------

# class Casa:
#     def __init__(self, area: int, rua: str, cor: str, nome: str =""):
#         self.Area = area
#         self.Rua = rua
#         self.Cor = cor
#         self.Nome = nome
        
#     def imprimirInfo (self):
#         if self.Nome == "" :
#             print(f'Area: {self.Area}, Rua: {self.Rua}, Cor: {self.Cor}')
#         else:
#             print(f'Area: {self.Area}, Rua: {self.Rua}, Cor: {self.Cor}, Morador: {self.Nome}')

        
# casaUm = Casa(120, 'Divina Providencia', 'vermelha', 'Mariana')

# Casa.imprimirInfo(casaUm)
# Casa.imprimirInfo(casaUm)
# Casa.imprimirInfo(casaUm)
# Casa.imprimirInfo(casaUm)
# Casa.imprimirInfo(casaUm)

#-------------------------------------------------------------------------------------------------------------------
# import math
# class Casa:
#     def __init__(self):
#         self.public='public'
#         self.__PI  = math.pi
        
#     def getPI (self):
#         return self.__PI
# casinha = Casa()

# print (casinha.public)

# print (casinha.getPI())

#-----------------------------------------------
class InstrumentoEscrita:
    def __init__(self, material):
        self.material = material
     
    def Escrever(self):
        print('escrevendo...')
    def Desenhar(self):
        print('desenhando...')
        
pai = InstrumentoEscrita("tinta")

class lapis(InstrumentoEscrita):
    def __init__(self):
        super().__init__("grafite")
        
class caneta(InstrumentoEscrita):
    def __init__(self):
        super().__init__('tinta')
    
    
print('Instrumento de escrita')
instrumento = InstrumentoEscrita('cera')
Lapis = lapis()
Lapis.Desenhar()