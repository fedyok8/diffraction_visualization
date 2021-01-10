#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys
import numpy as np
import random

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

        button_exit = QPushButton('Quit', self)
        button_exit.clicked.connect(
            QCoreApplication.instance().quit
        )
        button_exit.resize(button_exit.sizeHint())
        button_exit.move(900, 100)

        m = PlotCanvas(self, width=8, height=8)
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
        difraction = difraction_model()
        ax = self.figure.add_subplot(111)
        ax.plot(difraction['x'], difraction['I'])
        ax.set_title('difratcion on gap')
        self.draw()

def intensity(angle):
    if angle == 0:
        return 1
    else:
        b = 1 #mm (gap width)
        d = 10 #mm (diffraction grating period)
        wavelength = 450 #nm
        N = 4 #count of gaps

        b *= 1e-3
        d *= 1e-3
        if (b > d):
            print("error input parameters:\nb > d\nprogram aborted")
            sys.exit()
        wavelength *= 1e-7
        k = 2 * np.pi / wavelength
        u = k * b * np.sin(angle) / 2
        deltam = k * d * np.sin(angle) / 2

        return (
            np.sin(u)
            / u
            * np.sin(N * deltam)
            / np.sin(deltam)
        )**2

def difraction_model():
    points_count = 1000
    x1 = -1 #x is coordinate on screen
    x2 = 1
    L = 5 #lenth from gap to screen

    h = (x2 - x1) / points_count

    difraction = {
        'fi': np.zeros(points_count+1),
        'x': np.zeros(points_count+1),
        'I': np.zeros(points_count+1)
    }

    for i in range(points_count + 1):
        x = x1 + i * h
        angle = np.arctan(x / L)
        difraction['fi'][i] = angle
        difraction['x'][i] = x
        difraction['I'][i] = intensity(angle)
    return difraction


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())