#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QDesktopWidget,
    QMainWindow,
    QMenu,
    QVBoxLayout,
    QSizePolicy
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1000, 800)
        self.move_to_center()

        #if you want to define your own window geometry:
        # self.setGeometry(0, 0, 500, 500)

        self.setWindowTitle('Example window')
        self.setWindowIcon(QIcon('./app_icon.jpeg'))

        btn = QPushButton('Button1', self)
        btn.resize(btn.sizeHint())
        btn.move(900, 10)

        button_exit = QPushButton('Quit', self)
        button_exit.clicked.connect(
            QCoreApplication.instance().quit
        )
        button_exit.resize(button_exit.sizeHint())
        button_exit.move(900, 100)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Warning',
            'Are you sure to quit?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def move_to_center(self):
        window_rect = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_rect.moveCenter(center_point)
        self.move(window_rect.topLeft())

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())