import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import QPropertyAnimation,QRect,Qt
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QLabel,QPushButton,QDialog
import board
import traverse
import math
Form = uic.loadUiType(os.path.join(os.getcwd(),"main_window.ui"))[0]


class MainWindow(QMainWindow,Form):

    def initRandomTable(self):
        self.random_board=board.Board().getTable()
        
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
                    self.Tiles[i][j].setText(
                    '0'
                    )
                    self.Tiles[i][j].setVisible(False)       
    def changeTable(self,next_board,index):
        self.setupUi(self)
        self.Tiles=[[self.Tile_1,
                    self.Tile_2,
                    self.Tile_3],
                    [self.Tile_4,
                    self.Tile_5,
                    self.Tile_6],
                    [self.Tile_7,
                    self.Tile_8,
                    self.Tile_9]]
        self.solve_button.clicked.connect(self.solve)
        self.pushButton_next.clicked.connect(self.nextState)
        self.pushButton_prev.clicked.connect(self.prevState)
        self.lineEdit_Start.setInputMask("9 9 9 9 9 9 9 9 9")
        self.lineEdit_Goal.setInputMask("9 9 9 9 9 9 9 9 9")
        self.comboBox_Method.setCurrentIndex(index)
        def stringBoard(b):
            s=""
            for i in b:
                for j in i:
                    s+=str(j)
            return s
        self.lineEdit_Start.setText(stringBoard(next_board))
        self.pushButton_next.setEnabled(False)
        self.pushButton_prev.setEnabled(False)
               
        for i in range(0,3):
            for j in range(0,3):
                if next_board[i][j]!=0:
                    self.Tiles[i][j].setVisible(True)
                    self.Tiles[i][j].setText(
                    (str)(next_board[i][j])
                    )
                else:
                    self.Tiles[i][j].setText(
                    '0'
                    )
                    self.Tiles[i][j].setVisible(False)



    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.initRandomTable()
        self.solve_button.clicked.connect(self.solve)
        self.pushButton_next.clicked.connect(self.nextState)
        self.pushButton_prev.clicked.connect(self.prevState)
        self.lineEdit_Start.setInputMask("9 9 9 9 9 9 9 9 9")
        self.lineEdit_Goal.setInputMask("9 9 9 9 9 9 9 9 9")
        self.pushButton_next.setEnabled(False)
        self.pushButton_prev.setEnabled(False)
        
        def stringBoard(b):
            s=""
            for i in b:
                for j in i:
                    s+=str(j)
            return s
        self.lineEdit_Start.setText(stringBoard(self.random_board))
        self.lineEdit_Level.setInputMask("90")
        
      
    def moveTile(self,destination,location,direction,isNext):
        def swapPositionsInTileList(tlist,pos1, pos2): 
            tlist[pos1[0]][pos1[1]], tlist[pos2[0]][pos2[1]] = tlist[pos2[0]][pos2[1]], tlist[pos1[0]][pos1[1]]
            return tlist  
        i=location[0]
        j=location[1]
        self.animation=QPropertyAnimation(self.Tiles[i][j],b"geometry")
        self.animation.setDuration(100)
        
        self.animation.setStartValue(QRect(
            self.Tiles[i][j].x(),
            self.Tiles[i][j].y(),
            self.Tiles[i][j].width(),
            self.Tiles[i][j].height()
        ))

        self.animation.setEndValue(QRect(
            self.Tiles[i][j].x()+direction[1]*self.Tiles[i][j].width(),
            self.Tiles[i][j].y()+direction[0]*self.Tiles[i][j].height(),
            self.Tiles[i][j].width(),
            self.Tiles[i][j].height()
        ))
        self.animation.start()
        a=destination[0]
        b=destination[1]
        self.animation2=QPropertyAnimation(self.Tiles[a][b],b"geometry")
        self.animation2.setDuration(100)
        
        self.animation2.setStartValue(QRect(
            self.Tiles[a][b].x(),
            self.Tiles[a][b].y(),
            self.Tiles[a][b].width(),
            self.Tiles[a][b].height()
        ))

        self.animation2.setEndValue(QRect(
            self.Tiles[a][b].x()-direction[1]*self.Tiles[a][b].width(),
            self.Tiles[a][b].y()-direction[0]*self.Tiles[a][b].height(),
            self.Tiles[a][b].width(),
            self.Tiles[a][b].height()
        ))
        self.animation2.start()
        self.currentState+=isNext
        swapPositionsInTileList(self.Tiles,destination,location)
         


    def solve(self):
        if(self.lineEdit_Goal.hasAcceptableInput() and
            self.lineEdit_Start.hasAcceptableInput() and
            self.lineEdit_Level.hasAcceptableInput()):
            #correct input user
            
            def stringToTuple(string):
                a=[]
                string=list(string)
                for i in string:
                    if i != ' ':
                        a.append(int(i))
                return tuple(a)
            

            start = board.Board(stringToTuple(self.lineEdit_Start.text()))
            goal = board.Board(stringToTuple(self.lineEdit_Goal.text()))
            # self.Tiles=list(self.tempTiles)
            
            # print(start)
            # print(goal)
            


            if(self.comboBox_Method.currentIndex()==0):
                #dfsTraverse :
                dfs=traverse.DFSTraverseClass()
                self.sol=traverse.DFSTraverseClass.DFSTraverse(dfs,start,goal,(int)(self.lineEdit_Level.text()))
                a=([i.getTable() for i in self.sol])
                a.insert(0,start.getTable())
                self.sol=tuple(a)
            elif(self.comboBox_Method.currentIndex()==1):
                #bfsTraverse :
                self.sol=traverse.BFSTraverse(start,goal,(int)(self.lineEdit_Level.text()))
                b=[i.getTable() for i in self.sol]
                b.reverse()
                b.insert(0,start.getTable())
                self.sol=tuple(b)
            if self.sol.__len__()>1:
                self.changeTable(start.getTable(),self.comboBox_Method.currentIndex())
                self.currentState = 0
                self.pushButton_next.setEnabled(True)
                self.pushButton_prev.setEnabled(True)
                
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


            
    def nextState(self):
        def findZeroLocation(b):

            for i in range(0,3):
                for j in range(0,3):
                    if b[i][j] == 0:
                        return (i,j)
            
        if 0 <= self.currentState < self.sol.__len__()-1:
            a=findZeroLocation(self.sol[self.currentState])
            b=findZeroLocation(self.sol[self.currentState+1])

            def findMovementDirection(a,b):
                direction = (a[0]-b[0] , a[1]-b[1])
                return direction

            self.moveTile(a,b,findMovementDirection(a,b),1)
                    
    def prevState(self):
        def findZeroLocation(b):

            for i in range(0,3):
                for j in range(0,3):
                    if b[i][j] == 0:
                        return (i,j)
            
        if  1 <= self.currentState < self.sol.__len__():
            a=findZeroLocation(self.sol[self.currentState])
            b=findZeroLocation(self.sol[self.currentState-1])

            def findMovementDirection(a,b):
                direction = (a[0]-b[0] , a[1]-b[1])
                return direction

            self.moveTile(a,b,findMovementDirection(a,b),-1)    



    