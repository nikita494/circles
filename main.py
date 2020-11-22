import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from UI import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.draw_area.paintEvent = self.paint_area
        self.btn.clicked.connect(self.paint)

    def paint_area(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self.draw_area)
            qp.setPen(QColor(randrange(256), randrange(256), randrange(256)))
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
