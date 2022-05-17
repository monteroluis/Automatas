from PyQt5.QtGui import QPainterPath, QPainter

from Line import Line


class LineCurve(Line):

    def display(self):
      self.arrowhead()

    def arrowhead(self):
     self.qpaint.setRenderHint(QPainter.Antialiasing)
     if  self.initialY == self.endY:
        self.qpaint.drawLine(self.endX, self.endY, self.endX - 15, self.endY)
        self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY - 15)

     elif self.initialY < self.endY and self.initialX < self.endX:
         self.qpaint.drawLine(self.endX, self.endY, self.endX - 10, self.endY - 10)
         self.qpaint.drawLine(self.endX, self.endY, self.endX + 10, self.endY - 10)



     else:
        self.qpaint.drawLine(self.endX, self.endY, self.endX + 15, self.endY)
        self.qpaint.drawLine(self.endX, self.endY, self.endX, self.endY + 15)

    def setTipeCurve(self,tipe):

        if tipe == 1:
            tipe= self.initialY - 50
        else:
            tipe= self.initialY + 50

        path = QPainterPath()
        path.moveTo(self.initialX, self.initialY)
        path.cubicTo(self.initialX, self.initialY, (self.initialX + self.endX) / 2,tipe, self.endX,
                 self.endY)
        self.qpaint.drawPath(path)


