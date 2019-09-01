from PyQt5 import QtWidgets, QtGui
import sys, json
import urllib3
import models.app_state as app_state
from ui.ui import Ui_mainWindow as ResterUiWindow


class Rester(ResterUiWindow):
    def __init__(self):
        super().__init__()
        self.app_state = app_state.AppState()
        self.http = urllib3.PoolManager()

    def on_url_type_changed(self, text):
        self.app_state.request_attributes.request_type = text

    def handle_request_send(self):
        self.app_state.request_attributes.url = self.url.text()
        response = self.http.request('GET', self.app_state.request_attributes.url)
        raw_response = str(response.data)
        headers = response.headers

        self.response_raw.setText(raw_response)

        self.app_state.response_attributes.raw_response = raw_response
        self.app_state.response_attributes.headers = headers

        self.response_headers_table.setRowCount(len(headers))
        i = 0
        for key in headers:
            self.response_headers_table.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            self.response_headers_table.setItem(i, 1, QtWidgets.QTableWidgetItem(headers[key]))
            i += 1


def bind_actions(rester: Rester):
    # connect URL type combo box with internal variable
    rester.request_type.activated[str].connect(rester.on_url_type_changed)
    rester.send_btn.clicked.connect(rester.handle_request_send)


# Create an instance of QtWidgets.QApplication
app = QtWidgets.QApplication(sys.argv)

# Create an instance of QtWidgets.QMainWindow
mainWindow = QtWidgets.QMainWindow()

# Create an instance of our application class
rester_main_window = Rester()

# Bind Qt rendering of QtWidgets.QMainWindow with our main window
rester_main_window.setupUi(mainWindow)
bind_actions(rester_main_window)

# show it!
mainWindow.show()

# Without this line, the window of Rester will not show up
sys.exit(app.exec_())
