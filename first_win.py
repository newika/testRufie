from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class First_win(QWidget):
    def __init__(self):
        super().__init__()
        self.o_text = QLabel(text1)
        self.t_text = QLabel(text2)
        self.o_button = QPushButton(button1)
        self.line1 = QHBoxLayout()
        self.line2 = QHBoxLayout()
        self.line3 = QHBoxLayout()
        self.line1.addWidget(self.o_text, alignment = Qt.AlignLeft)
        self.line2.addWidget(self.t_text, alignment = Qt.AlignLeft)
        self.line3.addWidget(self.o_button, alignment = Qt.AlignCenter)
        self.line = QVBoxLayout()
        self.line.addLayout(line1)
        self.line.addLayout(line2)
        self.line.addLayout(line3)
        self.main_win.setLayout(line)
    def appl(self):
        self.main_win.setWindowTitle('Тест Руфье')
        self.main_win.move(900, 700)
        self.main_win.resize(400, 200)
        self.main_win.show()
    
app = QApplication([])
main_win = First_win()
main_win(appl)
app.exec_()