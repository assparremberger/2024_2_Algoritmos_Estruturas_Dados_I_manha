from Veiculo import Veiculo

class Carro( Veiculo ):

    def __init__(self, marca = None, portas = 4):
        super().__init__(marca)
        self.nPortas = portas

    def cadastrar(self):
        self._marca = input("Digite a marca: ")
        self.km = int( input("Digite a kilometragem: ") )
        self.nPortas = int( input("Quantidade de portas: ") )
    
    def __str__(self):
        txt = "\nPortas: " + str( self.nPortas )
        return super().__str__() + txt
