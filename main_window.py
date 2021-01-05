import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

Form = uic.loadUiType(os.path.join(os.getcwd(),"main_window.ui"))[0]


class MainWindow(QMainWindow,Form):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        




