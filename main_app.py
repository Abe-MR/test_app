import sys
from screenres import get_screen_resolution
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

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