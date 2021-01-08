#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(0, 0)
    w.setWindowTitle('diffraction')
    w.show()

    sys.exit(app.exec_())