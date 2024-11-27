from Livro import Livro

class Pilha:

    def __init__(self):
        self.topo = None
    
    def add( self, book ):
        if self.topo:
            book.prox = self.topo
        self.topo = book
        self.imprimir()
    
    def remover(self):
        if self.topo == None:
            print( "Nenhum elemento removido!")
        else:
            self.topo = self.topo.prox
        self.imprimir()

    def imprimir(self):
        print("\n*****Topo da Pilha*********")
        if self.topo == None:
            print("Pilha está vazia!")
        else:
            aux = self.topo
            while aux:
                print( aux )
                print("------------------------")
                aux = aux.prox
        print("******Base da Pilha*********")  

    