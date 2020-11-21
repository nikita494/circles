import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randrange


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.draw_area.paintEvent = self.paint_area
        self.btn.clicked.connect(self.paint)

    def paint_area(self, event):
        if self.do_paint:
            print('some')
            qp = QPainter()
            qp.begin(self.draw_area)
            qp.setPen(QColor(255, 255, 0))
            radius = randrange(25, 100)
            x, y = randrange(radius + 1, 625 - radius), randrange(radius + 1, 425 - radius)
            qp.drawEllipse(x, y, radius, radius)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.draw_area.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
