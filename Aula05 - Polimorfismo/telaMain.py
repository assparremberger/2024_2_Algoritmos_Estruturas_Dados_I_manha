import sys
from PyQt5.QtWidgets import QApplication
from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel

from Cidade import Cidade
from FormCidade import FormCidade

from Pessoa import Pessoa
from FormCliente import FormCliente

cidades = []
clientes = []

app = QApplication( sys.argv )

telaCid = FormCidade( listaCidades=cidades)
telaCid.show()

telaCli = FormCliente(  listaClientes=clientes, listaCidades=cidades)
telaCli.show()

sys.exit( app.exec_() )






#telaProduto = TelaProduto()
#telaProduto.show()

#telaPerecivel = TelaPerecivel()
#telaPerecivel.show()