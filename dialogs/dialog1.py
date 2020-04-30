import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        self.button.clicked.connect(self.greetings)
        self.label = QLabel("text")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        # Set dialog layout
        self.setLayout(layout)

    # Greets the user
    def greetings(self):
        print ("Hello {}".format(self.edit.text()))
        self.label.setText("Hello {}".format(self.edit.text()))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
