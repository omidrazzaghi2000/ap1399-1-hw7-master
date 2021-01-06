import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import QPropertyAnimation,QRect,Qt
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QLabel,QPushButton,QDialog
import board
import math
Form = uic.loadUiType(os.path.join(os.getcwd(),"main_window.ui"))[0]


class MainWindow(QMainWindow,Form):
    def initRandomTable(self):
        self.random_board=board.Board().getTable()
        print(self.random_board)
        self.Tiles=[[self.Tile_1,
                    self.Tile_2,
                    self.Tile_3],
                    [self.Tile_4,
                    self.Tile_5,
                    self.Tile_6],
                    [self.Tile_7,
                    self.Tile_8,
                    self.Tile_9]]
        for i in range(0,3):
            for j in range(0,3):
                if self.random_board[i][j]!=0:
                    self.Tiles[i][j].setText(
                    (str)(self.random_board[i][j])
                    )
                else:
                    self.Tiles[i][j].setVisible(False)       
    def changeTable(self,next_board):
        for i in range(0,3):
            for j in range(0,3):
                if next_board[i][j]!=0:
                    self.Tiles[i][j].setVisible(True)
                    self.Tiles[i][j].setText(
                    (str)(next_board[i][j])
                    )
                else:
                    self.Tiles[i][j].setVisible(False)

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.initRandomTable()
        self.solve_button.clicked.connect(self.solve)
        self.pButton_next.clicked.connect(self.move)
        self.lineEdit_Start.setInputMask("9 9 9 9 9 9 9 9 9")
        self.lineEdit_Goal.setInputMask("9 9 9 9 9 9 9 9 9")
        def stringBoard(b):
            s=""
            for i in b:
                for j in i:
                    s+=str(j)
            return s
        self.lineEdit_Start.setText(stringBoard(self.random_board))
        self.lineEdit_Level.setInputMask("99")
        
        
    def move(self):
        self.animation=QPropertyAnimation(self.Tiles[0][0],b"geometry")
        self.animation.setDuration(100)
        self.animation.setStartValue(QRect(
            self.Tiles[0][0].x(),
            self.Tiles[0][0].y(),
            self.Tiles[0][0].width(),
            self.Tiles[0][0].height()
        ))
        self.animation.setEndValue(QRect(
            self.Tiles[0][0].x()+self.Tiles[0][0].width(),
            self.Tiles[0][0].y(),
            self.Tiles[0][0].width(),
            self.Tiles[0][0].height()
        ))
        self.Tiles[0][0].move(90,0)
        self.animation.start()
        # self.Tiles[0][0].move(90,0)    


    def solve(self):
        if(self.lineEdit_Goal.hasAcceptableInput() and
            self.lineEdit_Start.hasAcceptableInput() and
            self.lineEdit_Level.hasAcceptableInput()):
            #correct input user
            print("ok")
        else:
            
            d = QDialog(self)
            
            
            d.setFixedSize(300,100)
            b1 = QPushButton("ok",d)
            b1.move(math.floor(d.width()/2)-math.floor(b1.width()/3),math.floor(d.height()/2))
            d.setWindowTitle("Dialog")
            l1 = QLabel("Please enter valid inputs ...",d)
            l1.move(math.floor(d.width()/2)-math.floor(l1.width()),math.floor(d.height()/3))
            b1.clicked.connect(lambda : d.close())
            d.setWindowModality(Qt.ApplicationModal)
            d.exec_()
            