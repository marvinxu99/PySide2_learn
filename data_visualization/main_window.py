import sys
from PySide2.QtGui import QKeySequence, QIcon
from PySide2.QtWidgets import QMainWindow, QAction, QApplication


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()

        self.initUI(widget)

    def initUI(self, widget):   
        self.setCentralWidget(widget)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Toolbar
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)
        self.setWindowTitle("Eartquakes information")
        self.setWindowIcon(QIcon('favicon.ico'))        

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()    
    sys.exit(app.exec_())    
