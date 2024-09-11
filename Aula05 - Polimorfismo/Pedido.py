from Pessoa import Pessoa
from Produto import Produto

class Pedido:

    def __init__(self, end, cliente=None):
        self.id = None
        self.end = end
        self.cliente = cliente
        self.__produtos = []

    def addProduto(self, prod):
        if prod is not None:
            self.__produtos.append(prod)
        soma = 0
        for p in self.__produtos:
            soma += p.preco
        return soma

    def __str__(self):
        txt = "Endereço: " + self.end
        txt += "\nCliente: " + str(self.cliente)
        txt += "\nProdutos: \n"
        for p in self.__produtos:
            txt += str(p) + "\n"
        return txt
    
    def imprimir(self):
        print( self )
        # print( self.__str__() )




