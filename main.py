#!/home/fedyok8/anaconda3/envs/pyqt/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(500, 500)
        self.move_to_center()

        #if you want to define your own window geometry:
        # self.setGeometry(0, 0, 500, 500)

        self.setWindowTitle('diffraction')
        self.setWindowIcon(QIcon('./app_icon.jpeg'))

        btn = QPushButton('Button1', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        button_exit = QPushButton('Quit', self)
        button_exit.clicked.connect(
            QCoreApplication.instance().quit
        )
        button_exit.resize(button_exit.sizeHint())
        button_exit.move(100, 100)

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

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())