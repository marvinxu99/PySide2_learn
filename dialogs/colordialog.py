import sys
from PySide2.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PySide2.QtGui import QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        col = QColor(0, 0, 0) 

        self.btn = QPushButton('Dialog - pick a colour', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(20, 60, 100, 100)            
        
        self.setGeometry(300, 300, 250, 380)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):
      
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ec = app.exec_()
    sys.exit(ec)