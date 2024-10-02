from PyQt5.QtWidgets import *
from Cliente import Cliente

class ListaClientes(QMainWindow):

    def __init__(self, listaClientes = [] , telaCliente = None ) :
        super().__init__()
        self.clientes = listaClientes
        self.telaCliente = telaCliente
        if self.telaCliente is not None:
            self.telaCliente.telaListaClientes = self

        self.setWindowTitle( "Clientes Cadastrados"  )
        self.setGeometry(100, 300, 600, 300)
        self.layout = QVBoxLayout()

        self.btnAbrirFormulario = QPushButton("Adicionar Cliente", self)
        self.btnAbrirFormulario.clicked.connect( self.abrirFormulario )
        self.layout.addWidget( self.btnAbrirFormulario )

        self.tabela = QListWidget(self)
        for cli in self.clientes:
            self.tabela.addItem( str(cli) , cli)
        self.layout.addWidget( self.tabela )

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def abrirFormulario(self):
        self.telaCliente.show()

    def atualizarTabela(self):
        self.tabela.clear()
        for cli in self.clientes:
            self.tabela.addItem( str(cli) )


