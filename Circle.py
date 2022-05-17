from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor, QPainter


class Circle:

    def __init__(self, qpaint, coordX, coordY, ratio):
        self.coordX = coordX;
        self.coordY = coordY;
        self.qpaint = qpaint
        self.ratio = ratio
        self.customize(Qt.cyan)

    def customize(self, color):
        pen = QPen(color)  # color de línea
        pen.setWidth(0)  # grosor de linea
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(color)
        self.qpaint.setBrush(brush)
        self.qpaint.setPen(pen)

    def display(self):
        self.qpaint.setRenderHint(QPainter.Antialiasing)
        self.qpaint.drawEllipse(self.coordX, self.coordY, self.ratio, self.ratio);

    def changeColor(self):
        self.customize(QColor(49, 49, 58, 255))  # color de la ventana
        self.display()
