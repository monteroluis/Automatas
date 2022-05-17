import sys
import time

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from Circle import Circle
from Line import Line
from LineCurve import LineCurve
from Validation import Validation
from design.interfaz import *


class Principal(QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        self.pintado = False;

    # self.ui.btnVerificar.clicked.connect(self.activate)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLine(qp)
        if self.activate():
            self.selectState(qp, self.getState())
            self.update()
        qp.end()

    def drawLine(self, qp):
        # Dibuja las lineas en la pantalla

        # 0-1
        line = Line(qp, 90, 260, 175, 260)
        line.display()

        # 1-2
        line = Line(qp, 200, 280, 285, 180)
        line.display()
        # 2-5
        line = Line(qp, 290, 160, 455, 160)
        line.display()
        # 1-3
        line = Line(qp, 220, 280, 280, 350)
        line.display()
        # 4-3
        line = Line(qp, 400, 260, 330, 345)
        line.display()
        # 6-4
        line = Line(qp, 480, 360, 420, 290)
        line.display()
        # 2-4
        line = Line(qp, 300, 160, 375, 240)
        line.display()

        # 5-7
        line = Line(qp, 490, 160, 570, 235)
        line.display()
        # 7-8
        line1 = LineCurve(qp, 615, 260, 698, 260)
        line1.setTipeCurve(1)
        line1.display()

        line2 = LineCurve(qp, 698, 270, 620, 271)
        line2.setTipeCurve(0)
        line2.display()

        # 5-6
        line = Line(qp, 490, 160, 490, 340)
        line.display()

        # 3-6
        line = LineCurve(qp, 340, 370, 455, 370)
        line.setTipeCurve(1)
        line.display()
        line = LineCurve(qp, 465, 391, 340, 390)
        line.setTipeCurve(0)
        line.display()

        # loop en 4
        line = LineCurve(qp, 400, 230, 420, 231)
        line.setTipeCurve(1)
        line.display()
        self.pintado = True;

    def selectState(self, qp, state):
        # posicion de boton con ajuste de  40 pixeles en Y

        if state == 0:
            nuevo = Circle(qp, 50, 230, 61)

        elif state == 1:
            nuevo = Circle(qp, 180, 230, 61)

        elif state == 2:
            nuevo = Circle(qp, 280, 130, 61)

        elif state == 3:
            nuevo = Circle(qp, 280, 340, 61)

        elif state == 4:
            nuevo = Circle(qp, 370, 230, 61)

        elif state == 5:
            nuevo = Circle(qp, 460, 130, 61)

        elif state == 6:
            nuevo = Circle(qp, 460, 340, 61)

        elif state == 7:
            nuevo = Circle(qp, 560, 230, 61)

        else:
            nuevo = Circle(qp, 700, 230, 61)
        for i in range(20):
            nuevo.display()
            self.update()

    def activate(self):
            valida = Validation()
            valida.validate(self.ui.lineEdit.text())
            return self.ui.lineEdit.text()

    def getState(self):
        return int(self.activate())

    def setState(self, state):
        return state


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Principal()
    win.show()
    sys.exit(app.exec_())
