import sys
from PyQt5.QtWidgets import QApplication
from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel

from Cidade import Cidade
from FormCidade import FormCidade

from Pessoa import Pessoa
from FormCliente import FormCliente

from ListaClientes import ListaClientes

cidades = []
clientes = []

app = QApplication( sys.argv )

telaCid = FormCidade( listaCidades=cidades)
#telaCid.show()

telaCli = FormCliente(  listaClientes=clientes, listaCidades=cidades, telaCidade=telaCid)
#telaCli.show()

telaListaClientes = ListaClientes( clientes , telaCli)
telaListaClientes.show()

sys.exit( app.exec_() )






#telaProduto = TelaProduto()
#telaProduto.show()

#telaPerecivel = TelaPerecivel()
#telaPerecivel.show()