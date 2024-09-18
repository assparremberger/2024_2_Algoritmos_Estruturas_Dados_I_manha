from TelaProduto import TelaProduto
from PyQt5.QtWidgets import QLineEdit, QLabel, QMessageBox
from Perecivel import Perecivel

class TelaPerecivel( TelaProduto ):
    def __init__(self, titulo = "Tela de Produto Perecível"):
        super().__init__(titulo)

    def construirLayout(self):
        super().construirLayout()
        self.lblTemperatura = QLabel("Temperatura Máxima: ")
        self.txtTemperatura = QLineEdit(self)
        self.layout.addWidget( self.lblTemperatura)
        self.layout.addWidget( self.txtTemperatura)
        self.setGeometry(450, 100, 300, 200)

    def salvar(self):
        perecivel = Perecivel( self.txtNome.text() )
        
        preco = self.txtPreco.text()
        if len(preco) > 0:
            preco = preco.replace( "," , "." )
            perecivel.preco = float( preco )

        temp = self.txtTemperatura.text()
        if len(temp) > 0:
            temp = temp.replace( "," , "." )
            perecivel.temperaturaMaxima = float( temp )

        QMessageBox.information( self , "Perecível Salvo" , str(perecivel) )

        # nome = self.txtNome.text()
        # preco = self.txtPreco.text()
        # temp = self.txtTemperatura.text()
        # fPreco = 0.0
        # if len(preco) > 0:
        #     preco = preco.replace( "," , "." )
        #     fPreco = float( preco )
        # txt = "Nome: " + nome + "\nPreço: " + str( fPreco )
        # txt += "\nTemperatura Máxima: " + temp 
        # QMessageBox.information( self , "Perecível Salvo" , txt )




