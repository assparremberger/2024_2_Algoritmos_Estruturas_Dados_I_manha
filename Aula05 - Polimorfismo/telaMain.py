import sys
from PyQt5.QtWidgets import QApplication
from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel

app = QApplication( sys.argv )

telaProduto = TelaProduto()
telaProduto.show()

telaPerecivel = TelaPerecivel()
telaPerecivel.show()

sys.exit( app.exec_() )