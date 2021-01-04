import sys
import os
# from main_window import MainWindow
# from PyQt5.QtWidgets import QApplication
import ctypes



if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # w=MainWindow()
    # w.show()
    # sys.exit(app.exec_())
    lib_path=os.path.join(os.getcwd(),'libboard.so')
    lib = ctypes.cdll.LoadLibrary(lib_path)
    print(lib)