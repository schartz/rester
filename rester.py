from PyQt5 import QtWidgets, uic
import sys


class RestApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RestApp, self).__init__()
        uic.loadUi('rester.ui', self)
        self.show()


# Create an instance of QtWidgets.QApplication
app = QtWidgets.QApplication(sys.argv)

# Create an instance of our class
window = RestApp()

# Start the application
app.exec_()
