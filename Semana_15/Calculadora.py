import sys
from PyQt5 import QtWidgets, uic, QtGui

class MiVentana(QtWidgets.QDialog):

    def __init__(self):
        super(MiVentana, self).__init__()
        uic.loadUi('calculadora.ui', self)
        self.BotonOperacion.clicked.connect(self.operar)
        self.show()

    def operacion(self, n1, n2, op):
        if op == "Sumar":
            return n1 + n2
        elif op == "Restar":
            return n1 - n2
        elif op == "Multiplicar":
            return n1 * n2
        elif op == "Dividir":
            if n2 == 0:
                return " OPERACIÓN NO SE PUEDE REALIZAR"
            else:
                return n1 / n2
        else:
            return " OPERACIÓN NO SOPORTADA"

    def operar(self):
        n1 = float(self.n1.value())
        n2 = float(self.n2.value())
        op = self.op.currentText()
        re = self.operacion(n1, n2, op)
        self.res.setText(str(re))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MiVentana()
    sys.exit(app.exec_())
