#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('diffraction')
        self.setWindowIcon(QIcon('./app_icon.jpeg'))

        btn = QPushButton('Button1', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())