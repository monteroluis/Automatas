from PyQt5.QtWidgets import QDialog
import sys
from design.configuraciones import Ui_Dialog
from design.interfaz import *


class Config(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)



    def execute(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec()


