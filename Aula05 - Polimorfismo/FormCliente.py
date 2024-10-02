import sys
from PyQt5.QtWidgets import *
from Cidade import Cidade
from Pessoa import Pessoa
#from FormCidade import FormCidade

class FormCliente(QMainWindow):

    def __init__(self, titulo="Cadastro de Cliente", listaClientes = [], listaCidades = [] , telaCidade = None ) :
        super().__init__()
        self.clientes = listaClientes
        self.cidades = listaCidades
        self.telaCidade = telaCidade
        self.telaListaClientes = None

        if self.telaCidade is not None:
            self.telaCidade.telaCliente = self

        self.setWindowTitle( titulo  )
        self.setGeometry(450, 100, 300, 200)
        self.layout = QVBoxLayout()
        self.construirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.__salvar )
        self.layout.addWidget( self.btnSalvar )

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def construirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget( self.lblNome)
        self.layout.addWidget( self.txtNome)

        self.lblAltura = QLabel("Altura: ")
        self.txtAltura = QLineEdit(self)
        self.layout.addWidget( self.lblAltura)
        self.layout.addWidget( self.txtAltura)

        # self.btnCarregarCidades = QPushButton("Atualizar lista de cidades", self)
        # self.btnCarregarCidades.clicked.connect( self.carregarCidades )
        # self.layout.addWidget( self.btnCarregarCidades )

        self.lblCidade = QLabel("Cidade: ")
        self.cmbCidade = QComboBox(self)
        self.cmbCidade.currentIndexChanged.connect( self.__abrirTelaCidade  )
        self.layout.addWidget( self.lblCidade )
        self.layout.addWidget( self.cmbCidade )
        self.carregarCidades()

    def __abrirTelaCidade(self):
        if self.cmbCidade.currentIndex() == 1:
            self.telaCidade.show()

    def carregarCidades(self):
        self.cmbCidade.clear()
        self.cmbCidade.addItem("Selecione...", None)
        self.cmbCidade.addItem("Adicionar nova Cidade...", None)
        for cid in self.cidades:
            self.cmbCidade.addItem( cid.nome , cid )

    def __salvar(self):
        if len( self.txtNome.text() ) > 0:
            cli = Pessoa( self.txtNome.text() )
            altura = self.txtAltura.text()
            if len( altura ) > 0:
                altura = altura.replace("," , ".")
                cli.altura = float( altura )
            if self.cmbCidade.currentIndex() > 1:
                cli.cidade = self.cmbCidade.currentData()
            self.clientes.append( cli )

            self.txtNome.clear()
            self.txtAltura.clear()
            self.cmbCidade.setCurrentIndex( 0 )
            QMessageBox.information(self, "Cliente Salvo" , str( cli ) )
            self.telaListaClientes.atualizarTabela()
            self.hide()