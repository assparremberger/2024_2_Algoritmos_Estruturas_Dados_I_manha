from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cid = Cidade("Itati")):
        self.id = None
        self.__nome = nome
        self.__altura = altura
        self.cidade = cid

    #Método acessor (Getter)
    def getNome(self):
        return self.__nome

    #Método Modificador (Setter)
    def setNome(self, valor):
        if len( valor ) > 0:
            self.__nome = valor
        else:
            print( "Valor inválido para o nome" )

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if len( valor ) > 0:
            self.__nome = valor
        else:
            print( "Valor inválido para o nome" )

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            print( "Valor inválido para a altura" )

    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nAltura: " + str(self.altura)
        txt += "\nCidade: " + self.cidade.nome
        return txt

    def cadastrar(self):
        self.nome = input("Digite o nome da Pessoa: ")
        self.altura = float( input("Digite a Altura: ") )
        return self
