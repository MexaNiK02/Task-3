import sys

from PyQt5 import uic  # Импортируем uic 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog, QGraphicsOpacityEffect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt
import random
import Ui # подключаем класс с файлом UI

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.paint)
        
    def initUI(self):
        Ui.Ui_Form.setupUi(self)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()      

    def draw_flag(self, qp):
        pen = QPen(Qt.yellow, 2)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        rad = random.randint(1, 250)
        qp.drawEllipse(100, 50, 50 + rad, 50 + rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
