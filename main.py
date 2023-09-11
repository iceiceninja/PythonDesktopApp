#   Do the below commands if it is your first time running the program (Not Moira)
#   Activate the virtual environment first...

#   .\venv\Scripts\activate 

#   Then download the PyQt package with the following command...

#   python -m pip install pyqt6 

#   BELOW IS HOW TO RUN THE PROGRAM

#   python .\main.py

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from button import button1_clicked
import sys


# 2. Create your application's GUI
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Hackathon")
        self.setWindowIcon(QtGui.QIcon('duck.jpeg'))

        helloMsg = QLabel("<h1>Hello, World!</h1>", parent=self)
        helloMsg.move(60, 15)
        button = QPushButton("Hello World", self)
        button.clicked.connect(button1_clicked)
        button.move(125, 150)
        self.input = QLineEdit(self)
        self.input.move(80, 100)



# 3. Create an instance of QApplication
app = QApplication(sys.argv)
window = Window()
# 4. Show your application's GUI
window.show()
# 5. Run your application's event loop
sys.exit(app.exec())