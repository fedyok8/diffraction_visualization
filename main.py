#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('diffraction')
        self.setWindowIcon(QIcon('./app_icon.jpeg'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())