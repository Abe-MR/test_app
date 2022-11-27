import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from screeninfo import get_monitors

def get_screen_resolution():
    width = 0
    height = 0
    for m in get_monitors():
        item = str(m).replace("(", "").replace(",", "").replace("=", " ")
        width = int(item.split(" ")[5])
        height = int(item.split(" ")[7])
        break
    return (width, height)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        
        # App size delcaration
        self.setMaximumSize(QSize(get_screen_resolution()[0], get_screen_resolution()[1]))
        self.setMinimumSize(QSize(400, 300))
        
        button = QPushButton("Click Here")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)
        
        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked!")
    
    def button_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()