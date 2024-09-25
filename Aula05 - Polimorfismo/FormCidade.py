import sys
from PyQt5.QtWidgets import *
from Cidade import Cidade

class FormCidade(QMainWindow):

    def __init__(self, titulo="Cadastro de Cidade", listaCidades = [] ) :
        super().__init__()
        self.cidades = listaCidades

        self.setWindowTitle( titulo  )
        self.setGeometry(100, 100, 300, 100)
        self.layout = QVBoxLayout()
        self.construirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def construirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget( self.lblNome)
        self.layout.addWidget( self.txtNome)

    def salvar(self):
        if len( self.txtNome.text() ) > 0:
            cid = Cidade( self.txtNome.text() )
            self.cidades.append( cid )
            self.txtNome.clear()
            QMessageBox.information(self, "Cidade Salva" , str( cid ) )