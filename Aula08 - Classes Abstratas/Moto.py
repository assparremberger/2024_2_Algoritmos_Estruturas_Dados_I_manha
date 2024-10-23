from Veiculo import Veiculo

class Moto( Veiculo ):

    def __init__(self, marca = None, cilindradas = 50):
        super().__init__(marca)
        self.cilindradas = cilindradas

    def cadastrar(self):
        self._marca = input("Digite a marca: ")
        self.km = int( input("Digite a kilometragem: ") )
        self.cilindradas = int( input("Cicindradas: ") )
    
    def __str__(self):
        txt = "_-:Motocicleta:-_"
        txt += "\nMarca: " + self._marca
        txt += "\nKm: " + str( self.__km )
        txt += "\nPortas: " + str( self.cilindradas )
        return txt
