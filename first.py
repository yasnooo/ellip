import sys

from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        self.is_draw = False
        super().__init__()
        uic.loadUi('рисовалка.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(5, 650)
        x, y = randint(5, 650), randint(5, 650)
        qp.drawEllipse(x - a // 2, y - a // 2, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
