from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Тест Руфье')
main_win.move(900, 700)
main_win.resize(400, 200)

text = QLabel('Добро пожаловать в программу вычисления работоспособности вашего сердца!')
text1 = QLabel('Перед началом прохождения этого теста советуем ознакомиться с инструкцией.')

button1 = QPushButton('Начать')

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(text, alignment = Qt.AlignLeft)
line2.addWidget(text1, alignment = Qt.AlignLeft)
line3.addWidget(button1, alignment = Qt.AlignCenter)

app.exec_()