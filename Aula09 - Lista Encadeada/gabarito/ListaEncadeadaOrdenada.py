from No import No

class ListaEncadeadaOrdenada:

    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("\n--------------------------------")
        if self.inicio == None:
            print( "\nLista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo 
        else:
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if nodo.dado < aux.dado :
                        ant.prox = nodo
                        nodo.prox = aux
                        break
                    ant = aux
                    aux = aux.prox
                if aux == None:
                    ant.prox = nodo
        self.imprimir()

    def remover(self, valor):
        if self.inicio == None:
            print( "Nenhum elemento removido" )
        else:
            encontrou = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                encontrou = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        encontrou = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
        if encontrou:
            print( valor , " foi encontrado e removido!")     
        else:
            print( valor , " não foi encontrado!") 
        self.imprimir()




    