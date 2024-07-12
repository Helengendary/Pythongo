class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descrição(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\n'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, porta):
        super().__init__(marca, modelo, ano)
        self.porta = porta
    
    def descrição(self):
        return super().descrição() + f'Portas: {self.porta}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def descrição(self):
        return super().descrição() + f'Cilindrada: {self.cilindrada}'
    
bb = int(input('1 - carro\n2 - Moto\n'))
print()
marca = input('Marca: ')
modelo = input('Modelo: ')
ano = input('Ano: ')

match bb:
    case 1:
        porta = input('Portas: ')
        carro = Carro(marca, modelo, ano, porta)
        print(carro.descrição())
    
    case 2:
        cilindrada = input('Cilindrada: ')
        moto = Moto(marca, modelo, ano, cilindrada)
        print(moto.descrição())