import sys
import os
from main_window import MainWindow
from PyQt5.QtGui import QImage,QPalette
from PyQt5.QtWidgets import QApplication
import ctypes
import board
import traverse

# a=board.Board(False)
# b=board.Board(False)
# t=traverse.DFSTraverseClass()
# c=traverse.DFSTraverseClass.DFSTraverse(t,a,b,10)

app = QApplication(sys.argv)
w=MainWindow()
w.show()
sys.exit(app.exec_())

    
    

    