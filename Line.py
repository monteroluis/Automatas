from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPainter, QBrush


class Line:

    def __init__(self, qpaint, initialX, initialY, endX, endY):
        self.initialX = initialX;
        self.initialY = initialY;
        self.endX = endX
        self.endY = endY
        self.qpaint = qpaint
        self.customize(Qt.black)

    def customize(self, color):
        pen = QPen(color)  # color de línea
        brush=QBrush()
        brush.setStyle(Qt.NoBrush)
        pen.setWidth(3)  # grosor de linea
        self.qpaint.setPen(pen)

    def display(self):
        self.qpaint.setRenderHint(QPainter.Antialiasing)
        self.qpaint.drawLine(self.initialX, self.initialY, self.endX, self.endY)
        self.arrowhead()

    def changeColor(self):
        self.customize(Qt.cyan)
        self.arrowhead()
        self.display()

    def arrowhead(self):

        # horizontal
        if self.initialY == self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 10, self.endY + 10)
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 10, self.endY - 10)

        # vertical hacia arriba
        elif self.initialX == self.endX and self.initialY > self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 10, self.endY + 10)
            self.qpaint.drawLine(self.endX, self.endY, self.endX + 10, self.endY + 10)

        # vertical hacia abajo
        elif self.initialX == self.endX and self.initialY < self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 10, self.endY - 10)
            self.qpaint.drawLine(self.endX, self.endY, self.endX + 10, self.endY - 10)

        # diagonal derecha-arriba
        elif self.initialX < self.endX and self.initialY > self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 15, self.endY)
            self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY + 15)

        # diagonal derecha-abajo
        elif self.initialX < self.endX and self.initialY < self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX - 15, self.endY)
            self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY - 15)

        elif self.initialX > self.endX and self.initialY < self.endY:
            self.qpaint.drawLine(self.endX, self.endY, self.endX + 15, self.endY)
            self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY - 15)

        else:
            self.qpaint.drawLine(self.endX, self.endY, self.endX + 15, self.endY)
            self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY + 15)
