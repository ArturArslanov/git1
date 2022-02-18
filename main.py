import sys

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from UI import MyWidget
from random import randint


class Example(QMainWindow, MyWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.tr = False
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Рисование')
        self.coords = randint(0, 450), randint(0, 350)
        self.pushButton.clicked.connect(self.any)
        self.s1 = []

    def any(self):
        self.tr = True
        self.repaint()

    def paintEvent(self, event) -> None:
        if self.tr:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.coords = randint(0, 600), randint(0, 400)
        size_1 = randint(10, 151)
        self.s1.append((self.coords[0] - size_1 / 2,
                        self.coords[-1] - size_1 / 2, size_1, size_1, color))
        for i in self.s1:
            qp.setBrush(QColor(*i[-1]))
            qp.drawEllipse(*i[:4])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
