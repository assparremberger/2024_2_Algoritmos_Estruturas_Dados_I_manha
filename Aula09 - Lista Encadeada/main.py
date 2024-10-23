from ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()

lista.imprimir()
lista.addInicio( "Guilherme" )
lista.addInicio( "Daniel" )
lista.addFim( "João" )
lista.addInicio( "Camila" )
lista.addFim( "Leonardo" )

lista.removerInicio()
lista.removerFim()

lista.remover("Guilherme")
lista.remover("Adalto")
