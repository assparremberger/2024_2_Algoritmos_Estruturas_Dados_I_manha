from Produto import Produto
from Categoria import Categoria

class Perecivel(Produto):

    def __init__(self, nomeP, precoP=5.0, catP = Categoria("Congelados"), tempMax=7 ):
        #super().__init__(nomeP, cat=catP)
        super().__init__(nomeP, precoP, catP)
        self.temperaturaMaxima = tempMax

    def __str__(self):
        txt = super().__str__()
        txt += "\nTemperatura Máxima: " + str(self.temperaturaMaxima)
        return txt

    def cadastrar(self):
        self = super().cadastrar()
        temp = input("Digite a temperatura máxima: ") 
        self.temperaturaMaxima = float( temp )
        return self
      