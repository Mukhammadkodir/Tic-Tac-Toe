import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
class MainWindow(QWidget):
    def __init__(self):
        super(). __init__()
        
       
        #main methods
        self.setStyleSheet('.QLabel { font-size: 20pt;}')
        self.v_box = QVBoxLayout()
        self.hh_box = QHBoxLayout()
        self.h_box = QHBoxLayout()
        self.h0_box = QHBoxLayout()
        self.h1_box = QHBoxLayout()
        self.h2_box = QHBoxLayout()
        self.h3_box = QHBoxLayout()
        self.h4_box = QHBoxLayout()
        self.label = QLabel()
        self.label2 = QLabel()
        self.edit = QLineEdit()
        


        #buttons
        self.btn1 = QPushButton(" 1 ")
        self.btn2 = QPushButton(" 2 ")
        self.btn3 = QPushButton(" 3 ")
        self.btn4 = QPushButton(" 4 ") 
        self.btn5 = QPushButton(" 5 ")
        self.btn6 = QPushButton(" 6 ")
        self.btn7 = QPushButton(" 7 ")
        self.btn8 = QPushButton(" 8 ") 
        self.btn9 = QPushButton(" 9 ")
        self.btn0 = QPushButton(" 0 ")

        self.btn_qosh = QPushButton(" + ")
        self.btn_ayir = QPushButton(" - ")
        self.btn_kopaytir = QPushButton(" x ")
        self.btn_bol = QPushButton(" ÷ ") 
        self.btn_javob = QPushButton(" = ")
        self.btn_tozala = QPushButton(" AC ")
        self.btn_float = QPushButton(" . ")

        self.btn_del = QPushButton(" Delate ")

        #button colors
        self.btn1.setStyleSheet("background-color: grey")
        self.btn2.setStyleSheet("background-color: grey")
        self.btn3.setStyleSheet("background-color: grey")
        self.btn4.setStyleSheet("background-color: grey")
        self.btn5.setStyleSheet("background-color: grey")
        self.btn6.setStyleSheet("background-color: grey")
        self.btn7.setStyleSheet("background-color: grey")
        self.btn8.setStyleSheet("background-color: grey")
        self.btn9.setStyleSheet("background-color: grey")
        self.btn0.setStyleSheet("background-color: grey")
        

        self.btn_qosh.setStyleSheet("background-color: orange")
        self.btn_ayir.setStyleSheet("background-color: orange")
        self.btn_kopaytir.setStyleSheet("background-color: orange")
        self.btn_bol.setStyleSheet("background-color: orange")
        self.btn_javob.setStyleSheet("background-color: orange")

        self.btn_tozala.setStyleSheet("background-color: darkGray")
        self.btn_float.setStyleSheet("background-color: orange")
        self.btn_del.setStyleSheet("background-color: darkGray")
        self.label.setStyleSheet("font-weight: bold")


        #horizantel
        self.h_box.addWidget(self.label)
        self.hh_box.addWidget(self.label2)

        #horizantel0
        self.h0_box.addWidget(self.btn_tozala)
        self.h0_box.addWidget(self.btn_del)

        #horizantel1
        self.h1_box.addWidget(self.btn1)
        self.h1_box.addWidget(self.btn2)
        self.h1_box.addWidget(self.btn3)
        self.h1_box.addWidget(self.btn_qosh)


        #horizantel2
        self.h2_box.addWidget(self.btn4)
        self.h2_box.addWidget(self.btn5)
        self.h2_box.addWidget(self.btn6)
        self.h2_box.addWidget(self.btn_ayir)

        #horizantel3
        self.h3_box.addWidget(self.btn7)
        self.h3_box.addWidget(self.btn8)
        self.h3_box.addWidget(self.btn9)
        self.h3_box.addWidget(self.btn_kopaytir)

        #horizantel4
        self.h4_box.addWidget(self.btn_float)
        self.h4_box.addWidget(self.btn0)
        self.h4_box.addWidget(self.btn_bol)
        self.h4_box.addWidget(self.btn_javob)
        self.hh_box.addWidget(self.label2)
        
        #add horizantels in vertikal
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.hh_box)
        self.v_box.addLayout(self.h0_box)
        self.v_box.addLayout(self.h1_box)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addLayout(self.h4_box)
        #self.v_box.addLayout(self.hh_box)

        #giving events------
        self.btn1.clicked.connect(self.print1)
        self.btn2.clicked.connect(self.print2)
        self.btn3.clicked.connect(self.print3)
        self.btn4.clicked.connect(self.print4)
        self.btn5.clicked.connect(self.print5)
        self.btn6.clicked.connect(self.print6)
        self.btn7.clicked.connect(self.print7)
        self.btn8.clicked.connect(self.print8)
        self.btn9.clicked.connect(self.print9)
        self.btn0.clicked.connect(self.print0)

        self.btn_qosh.clicked.connect(self.qoshish)
        self.btn_ayir.clicked.connect(self.ayrish)
        self.btn_kopaytir.clicked.connect(self.kopaytir)
        self.btn_bol.clicked.connect(self.bolish) 
        self.btn_javob.clicked.connect(self.barobar)
        self.btn_tozala.clicked.connect(self.tozala2)
        self.btn_float.clicked.connect(self.print_point)
        self.btn_del.clicked.connect(self.orqaga)
    
        #add fun to out window
        self.setLayout(self.v_box)
        self.setWindowTitle("Calculator")
        #self.setWindowIcon(QtGui.QIcon("calculator.png"))
        self.setGeometry(500,300,300,300)

        #out to window
        self.show()

        #methods----------
    def barobar(self):

        expression = self.label.text()
        try:
            javob = eval(expression)
            self.label2.setText(str(javob))
        except ZeroDivisionError:
            self.label2.setText("Infinity")
        except SyntaxError:
            self.label2.setText("Error")
        except :
            self.label2.setText("Error")

    def qoshish(self):
        expression = self.label.text()
        size = len(expression)
        if expression[size-1] == '+' or expression[size-1] == "-" or expression[size-1] == '/' or expression[size-1] == '*':
             expression = expression[:-1]
             self.label.setText(expression + "+")
        else:
            self.label.setText(expression + "+")

    def ayrish(self):
        expression = self.label.text()
        size = len(expression)
        if expression[size-1] == '+' or expression[size-1] == "-" or expression[size-1] == '/' or expression[size-1] == '*':
             expression = expression[:-1]
             self.label.setText(expression + "-")
        else:
            self.label.setText(expression + "-")

    def bolish(self):
        expression = self.label.text()
        size = len(expression)
        if expression[size-1] == '+' or expression[size-1] == "-" or expression[size-1] == '/' or expression[size-1] == '*':
             expression = expression[:-1]
             self.label.setText(expression + "/")
        else:
            self.label.setText(expression + "/")

    def kopaytir(self):
        expression = self.label.text()
        size = len(expression)
        if expression[size-1] == '+' or expression[size-1] == "-" or expression[size-1] == '/' or expression[size-1] == '*':
             expression = expression[:-1]
             self.label.setText(expression + "*")
        else:
            self.label.setText(expression + "*")

    def print_point(self):
        expression = self.label.text()
        self.label.setText(expression + ".")



    #printing numbers
    def print0(self):
        expression = self.label.text()
        self.label.setText(expression + "0")

    def print1(self):
        expression = self.label.text()
        self.label.setText(expression + "1")

    def print2(self):
        expression = self.label.text()
        self.label.setText(expression + "2")

    def print3(self):
        expression = self.label.text()
        self.label.setText(expression + "3")

    def print4(self):
        expression = self.label.text()
        self.label.setText(expression + "4")

    def print5(self):
        expression = self.label.text()
        self.label.setText(expression + "5")

    def print6(self):
        expression = self.label.text()
        self.label.setText(expression + "6")

    def print7(self):
        expression = self.label.text()
        self.label.setText(expression + "7")

    def print8(self):
        expression = self.label.text()
        self.label.setText(expression + "8")

    def print9(self):
        expression = self.label.text()
        self.label.setText(expression + "9")

    def tozala2(self):
        self.label.setText("")
        self.label2.setText("")

    def orqaga(self):
        expression = self.label.text()
        self.label.setText(expression[:-1])
   

app = QApplication([])
a = MainWindow()
sys.exit(app.exec_())