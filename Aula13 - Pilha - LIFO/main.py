from Livro import Livro
from Pilha import Pilha

pilha = Pilha()

pilha.imprimir()

l1 = Livro("O tempo e o vento", "Érico Veríssimo", 1000 )
l2 = Livro("Dom Casmurro", "Machado de Assis", 500 )
l3 = Livro("Memórias póstumas de Brás Cubas", "Machado de Assis", 700)

pilha.add( l1 )
pilha.add( l3 )
pilha.add( l2 )

pilha.remover()