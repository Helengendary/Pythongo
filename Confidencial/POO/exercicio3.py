class Banco:
    __numerosContas = 0
    
    def __init__(self, cliente, agencia, nmrConta, tipoConta, saldo=0):
        self.__cliente = cliente
        self.__agencia = agencia
        self.__nmrConta = nmrConta
        self.__saldo = saldo
        self.__tipoConta = tipoConta
        Banco.__numerosContas += 1
        
        
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, valor):
        self.__saldo += valor
    
    def getCliente(self):
        return self.__cliente
    
    def getAgencia(self):
        return self.__agencia
    
    def getNmrConta(self):
        return self.__nmrConta
    
    def getTipoConta(self):
        return self.__tipoConta
      
    @staticmethod        
    def numeroContas():
        print(Banco.__numerosContas)

cliente1 = Banco('Helena', '1234-5', '67890', 'Corrente')
cliente1.setSaldo(1000000000000000000000000000000000000000000000000000)
print(f'Saldo de {cliente1.getCliente()}: {cliente1.getSaldo()}')

cliente2 = Banco('Adrian', '5432-1', '09876', 'Poupança')
cliente2.setSaldo(19999999999999999999999)
print(f'Saldo de {cliente2.getCliente()}: {cliente2.getSaldo()}')