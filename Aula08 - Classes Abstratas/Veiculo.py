from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca):
        self.id = None
        self._marca = marca
        self.__km = 0

    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self, valor):
        if valor > self.__km:
            self.__km = valor
        else:
            print("Valor não permitido!")

    @abstractmethod
    def cadastrar(self):
        pass

    def __str__(self):
        txt = "Marca: " + self._marca
        txt += "\nKm: " + str( self.__km )
        return txt
    
    def imprimir(self):
        print( self )