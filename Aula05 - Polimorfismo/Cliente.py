from Cidade import Cidade
from Pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, altura = 1.73, cid = None, limite = 1000):
        super().__init__(nome, altura, cid)
        self.limite = limite

    def __str__(self):
        txt = super().__str__()
        txt += "\nLimite: R$ " + str(self.limite)
        return txt

    def cadastrar(self):
        self.nome = input("Digite o nome do Cliente: ")
        self.altura = float( input("Digite a altura do cliente: ") )
        nomeCid = input("Digite o nome da Cidade do cliente: ")
        self.cidade = Cidade( nomeCid )
        self.limite = float( input("Digite o valor do limite: ") )
        return self


    
