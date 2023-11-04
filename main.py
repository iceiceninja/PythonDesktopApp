# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from button import button1_clicked
import sys


# 2. Create your application's GUI
class Window(QWidget):
    def __init__(self):
        outerBoxLayout = QVBoxLayout()
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Hackathon")
        self.setWindowIcon(QtGui.QIcon('duck.jpeg'))

        outerBoxLayout.addWidget(QLabel("<h1>Organizer9000</h1>"),1)
        outerBoxLayout.addWidget(QLineEdit())
        innerBoxLayout = QHBoxLayout()
        innerVBoxLayout = QVBoxLayout()
        innerVBoxLayout.addWidget(QLabel("<h1>TOP LEFT</h1>"))
        innerVBoxLayout.addWidget(QLabel("<h1>BOTTOM LEFT</h1>"))
        innerBoxLayout.addLayout(innerVBoxLayout)
        # innerBoxLayout.addWidget(QLabel("<h1>BottomLeftBOx</h1>"))
        innerBoxLayout.addWidget(QLabel("<h1>BottomRightbox</h1>"))
        outerBoxLayout.addLayout(innerBoxLayout)
        self.setLayout(outerBoxLayout)
        # helloMsg = QLabel("<h1>Hello, World!</h1>", parent=self)
        # helloMsg.move(60, 15)
        # button = QPushButton("Hello World", self)
        # button.clicked.connect(button1_clicked)
        # button.move(125, 150)
        # self.input = QLineEdit(self)
        # self.input.move(80, 100)



# 3. Create an instance of QApplication
app = QApplication(sys.argv)
window = Window()
# 4. Show your application's GUI
window.show()
# 5. Run your application's event loop
sys.exit(app.exec())