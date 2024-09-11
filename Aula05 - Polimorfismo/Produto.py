from Categoria import Categoria

class Produto:
    def __init__(self, nome, preco = 10.0, cat = Categoria("Bebidas")):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat
    
    def __str__(self):
        txt = "--------------------"
        txt += "\nNome: " + self.nome
        txt += "\nPreço: " + str(self.preco)
        txt += "\nCategoria: " + self.categoria.nome
        return txt

    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.preco = float( input("Digite o preço: ") )
        return self
