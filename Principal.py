import sys
import time
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPixmap, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication
import Speak
from Circle import Circle
from Config import Config
from Line import Line
from LineCurve import LineCurve
from Validation import Validation
from design.interfaz import *
import gettext

idiomas = ['fr_FR']
t = gettext.translation('principal', 'locale', languages=idiomas, fallback=True)
_ = t.gettext


class Principal(QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        self.ui.btnVerificar.clicked.connect(lambda: self.hacer())
        self.ui.btnconfiguraciones.clicked.connect(lambda: self.settings())
        habla = Speak
        habla.voice("ingresa la palabra que deseas validar", "es")


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLine(qp)
        qp = QPainter()
        qp.begin(self)
        self.drawLine(qp)
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

    def restore(self):
        self.ui.estado_0.setStyleSheet("Background-color:#1CFF2F")
        self.ui.estado_1.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_2.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_3.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_4.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_5.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_6.setStyleSheet("Background-color:#318CE7")
        # nuevo = Circle(qp, 560, 230, 61)
        self.ui.estado_7.setStyleSheet("Background-color:#318CE7")
        self.ui.estado_8.setStyleSheet("Background-color:#318CE7")

    def selectState(self, state):
        #  def selectState(self, qp, state):
        # posicion de boton con ajuste de  40 pixeles en Y

        if state == 0:
            self.ui.estado_0.setStyleSheet("Background-color:#1CFF2F")

        # nuevo = Circle(qp, 50, 230, 61)

        elif state == 1:
            # nuevo = Circle(qp, 180, 230, 61)
            self.ui.estado_1.setStyleSheet("Background-color:#1CFF2F")

        elif state == 2:
            # nuevo = Circle(qp, 280, 130, 61)
            self.ui.estado_2.setStyleSheet("Background-color:#1CFF2F")
        elif state == 3:
            # nuevo = Circle(qp, 280, 340, 61)
            self.ui.estado_3.setStyleSheet("Background-color:#1CFF2F")
        elif state == 4:
            # nuevo = Circle(qp, 370, 230, 61)
            self.ui.estado_4.setStyleSheet("Background-color:#1CFF2F")
        elif state == 5:
            # nuevo = Circle(qp, 460, 130, 61)
            self.ui.estado_5.setStyleSheet("Background-color:#1CFF2F")
        elif state == 6:
            # nuevo = Circle(qp, 460, 340, 61)
            self.ui.estado_6.setStyleSheet("Background-color:#1CFF2F")
        elif state == 7:
            # nuevo = Circle(qp, 560, 230, 61)
            self.ui.estado_7.setStyleSheet("Background-color:#1CFF2F")
        else:
            # nuevo = Circle(qp, 700, 230, 61)
            self.ui.estado_8.setStyleSheet("Background-color:#1CFF2F")

    def hacer(self):
        nueva = Validation()
        palabra = self.ui.lineEdit.text()
        res = nueva.validate(self.ui.lineEdit.text())

        if res == 0:
            self.ui.valoracion.setText(_("Aceptada"))

            self.ui.valoracion.setStyleSheet("color:green;font-size:25px")
            habla = Speak
            habla.voice(_(palabra + "es Aceptada"), "es")

        else:
            self.ui.valoracion.setText(_("Rechazada"))
            self.ui.valoracion.setStyleSheet("color:red;font-size:25px")
            habla = Speak
            habla.voice(_("Rechazada"), "es")
        self.restore()
        for i in nueva.arrayStates:
            self.selectState(i)

    def settings(self):
        nuevo = Config()
        nuevo.execute()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Principal()
    win.show()
    sys.exit(app.exec_())
