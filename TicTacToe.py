import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton,QRadioButton, QWidget, QVBoxLayout, QGridLayout, qApp
from buttons import mybutton
from PyQt5.QtGui import *


class mainwindow(QWidget):
    EXIT_CODE_REBOOT = -123

    def __init__(self):
        super().__init__()
        self.gamer = None

        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 200, 500)
        self.setStyleSheet("background-color : #2C7878")
        
        self.vout1 = QVBoxLayout()
        self.vout2 = QVBoxLayout()
        self.vout3 = QVBoxLayout()
        self.player_x = QRadioButton("X-begin")
        self.player_0 = QRadioButton("o-begin")
        self.player_0.setStyleSheet("background-color : #8DACA7")
        self.player_x.setStyleSheet("background-color : #8DACA7")
        self.layout = QGridLayout()
        self.start_btn = QPushButton("START")
        self.start_btn.setStyleSheet("background-color : #8DACA7")

        self.buttons = [mybutton(i) for i in range(9)]
        pos = [(i, j) for i in range(3) for j in range(3)]
        self.layout.addWidget(self.player_x, 20, 0)
        self.layout.addWidget(self.player_0, 20, 2)
        self.layout.addWidget(self.start_btn, 30, 50)
        self.player_x.toggled.connect(self.p_x)
        self.player_0.toggled.connect(self.p_0)
        self.start_btn.clicked.connect(self.start_game)

        for btn, p in zip(self.buttons, pos):
            btn.setFixedHeight(100)
            btn.setFixedWidth(100)
            btn.setFont(QFont(QFont('Times', 30)))
            self.layout.addWidget(btn, *p)
            btn.clicked.connect(self.p)

        self.setLayout(self.layout)
        self.show()

        
    def p(self):
        btn = self.sender()
        btn.setText(self.gamer)
        
        btn.setStyleSheet("background-color : #609893")
        btn.setDisabled(True)
        self.gamer = not self.gamer
        self.checker()

    def checker(self):
        if self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() != "":
            self.showDialog(self.buttons[3].text())
        elif self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[6].text())
        elif self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() != "":
            self.showDialog(self.buttons[1].text())
        elif self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[2].text())
        elif self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() != "":
            self.showDialog(self.buttons[2].text())
        elif not self.buttons[0].text() == "" and not self.buttons[1].text() == "" and not self.buttons[2].text() == "" and not self.buttons[3].text() == "" and  not self.buttons[4].text() == "" and not self.buttons[5].text() == "" and  not self.buttons[6].text() == "" and not self.buttons[7].text() == "" and not self.buttons[8].text() == "":
            self.showDialog("None")

    def showDialog(self, player_win):
        self.player_win = player_win
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        if not self.player_win == 'None':
            buttonReply = QMessageBox.question(self, 'Winner tabel', f"{self.player_win} is win in this game\nDo you want to paly again", QMessageBox.Ok | QMessageBox.Cancel)
        else:
            buttonReply = QMessageBox.question(self, 'Winner tabel', f"Draw\nDo you want to paly again", QMessageBox.Ok | QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            self.retry_game()
        else:
            sys.exit(app.exec_())
    
    @staticmethod
    def retry_game():
        qApp.exit(mainwindow.EXIT_CODE_REBOOT)

    def start_game(self):
        for i in range(len(self.buttons)):
            self.buttons[i].setDisabled(False)
        self.start_btn.setText("RETRY")
        self.start_btn.setStyleSheet("background-color : #2F8282")
        self.start_btn.clicked.connect(self.retry_game)

    def p_x(self):
        self.start_btn.setDisabled(False)
        self.gamer = True

    def p_0(self):
        self.start_btn.setDisabled(False)
        self.gamer = False
       

if __name__=="__main__":
    currentExitCode = mainwindow.EXIT_CODE_REBOOT
    while currentExitCode == mainwindow.EXIT_CODE_REBOOT:
        app = QApplication([])
        win = mainwindow()
        currentExitCode = app.exec_()
        app = None