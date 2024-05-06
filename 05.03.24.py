# class instrumentoEscrita():
#     def __init__(self, material):
#         self.material = material
        
#     def Escrevendo (self):
#         print('Escrevendo...')
#     def Desenhar (self):
#         print('Desenhando...')
        
# instrumento = instrumentoEscrita('tinta')

# class Lapis (instrumentoEscrita):
#     def __init__(self):
#         super().__init__('grafite')
        
#-------------------------------------------------
# class personagem:
#     _vida = 0
#     _força = 0
#     _inteligencia = 0
#     _dinheiro_por_min = 0
    
#     def __init__(self):
#         self._vida = 100
#         self._força = 10
#         self._inteligencia = 10
#         self._dinheiro_por_min = 10
#         pass
    
#     def Ataque(self):
#         return self._força
    
#     def getVida(self):
#         return self._vida
    
    
    
# class globin(personagem):
#     def __init__(self):
#         super().__init__()
#         self._força = 14
#         self._inteligencia = 9
#         self._dinheiro_por_min = 11
        
# random = personagem()
# print(f'Vida de um personagem aleatório: {random.getVida()}')    
# print(f'Força de mineração: {random.Ataque()}')        
        
# g = globin()
# print(f'A vida de um globin {g.getVida()}')
# print(f'Força de mineração {g.Ataque()}')

#----------------------------------------------------------------------------------------------------   
# import math

# class Calculadora:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def Soma(self):
#         print(f'{self.a} + {self.b} = {self.a + self.b}')
        
#     def Subtracao(self):
#         print(f'{self.a} - {self.b} = {self.a - self.b}')
        
#     def Divisao(self):
#         print(f'{self.a} / {self.b} = {self.a / self.b}')
        
#     def Multiplicacao(self):
#         print(f'{self.a} * {self.b} = {self.a * self.b}')
        
#     def Quadrado(self):
#         print(f'{self.a}^2 = {self.a ** 2}')
        
#     def Raiz(self):
#         print(f'√{self.a} = {math.sqrt(self.a)}')
        
# class CalculadoraCientifica(Calculadora):
#     def __init__(self, a, b):
#         super().__init__(a, b)
    
#     def log(self):
#         print(math.log(self.a))
        
#     def PI(self):
#         print(f'O valor de pi: {math.pi}')
        
#     def fatorial(self):
#         print(math.factorial(self.a))

# while True:
#     try:    
#         choice = int(input('\nQual calculadora deseja usar\n1 - calculadora normal\n2 - calculadora científica\n'))
#         if choice == 1 or choice == 2:
#             break
#         else:
#             print('Digite um número válido!')
#     except ValueError:
#         print('Digite um número!')
# match choice:
#     case 1:
#         op = int(input('\n1 - soma\n2 - subtração\n3 - divisão\n4 - multiplicação\n5 - quadrado\n6 - Raiz quandrada\n'))
#         while True:
#             try:
#                 num1 = int(input('Qual o primeiro número: '))
#                 num2 = int(input('Qual o segundo número: '))
#                 break        
#             except ValueError:
#                 print('Digite um número!')
            
#         calculadora = Calculadora(num1, num2)
#         match op:
#             case 1:
#                 print(calculadora.Soma())
#             case 2:
#                 print(calculadora.Subtracao())
#             case 3: 
#                 print(calculadora.Divisao())
#             case 4:
#                 print(calculadora.Multiplicacao())
#             case 5: 
#                 print(calculadora.Quadrado())
#             case 6:
#                 print(calculadora.Raiz())
#     case 2:
#         op = int(input('\n1 - log\n2 - pi\n3 - fatorial\n'))
#         num = int(input('Digite um número:\n'))
#         cientifica = CalculadoraCientifica(num, 0)
#         match op:
#             case 1:
#                 print(cientifica.log())
#             case 2:
#                 print(cientifica.PI())
#             case 3: 
#                 print(cientifica.fatorial())

#------------------------------------------------------------------------------------------------------------------------------------------------------------
class Conta():
    def __init__(self, dono, saldo= 0.0):
        self.dono = dono
        self.saldo = saldo
        
    def getSaldo(self):
        return self.saldo
    
class ContaTransferencia():
    def __init__(self, dono, saldo= 0.0):
        self.dono = dono
        self.saldo = saldo
    
    def Transferir(self):
        transferir = float(input('Qual valor deseja transferir: '))
        if transferir > self.saldo: 
            print('Saldo insuficiente!')
        else:
            print(f'Seu saldo ficou: {self.saldo - transferir}')
        
    def depositar(self):
        self.deposito = float(input('Qual valor você quer depositar na conta poupança: '))
        print(f'Seu saldo ficou: {self.saldo + self.deposito}')
        
class Poupanca(ContaTransferencia):
    def __init__(self, dono, saldo):
        super().__init__(dono, saldo)
    
class Salario(Conta):
    def __init__(self, dono, saldo):
        super().__init__(dono, saldo)
    
class Corrente(ContaTransferencia):
    def __init__(self, dono, saldo):
        super().__init__(dono, saldo)        
    
conta = Poupanca('helena', 1000)
conta.depositar()