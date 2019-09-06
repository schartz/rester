import sys
import urllib3

from PyQt5 import QtWidgets
from fbs_runtime.application_context.PyQt5 import ApplicationContext

import src.main.python.models.app_state as app_state
from src.main.python.threads.http import HttpThread
from src.main.python.ui.ui import Ui_mainWindow as ResterUiWindow


class Rester(ResterUiWindow):
    def __init__(self):
        super().__init__()
        self.app_state = app_state.AppState()

    def on_url_type_changed(self, text: str) -> None:
        self.app_state.request_attributes.request_type = text

    def handle_request_send(self):
        self.clear_ui_before_request()
        self.app_state.request_attributes.url = self.url.text()
        self.request_thread = HttpThread(self.app_state.request_attributes)
        self.request_thread.request_completed.connect(self.update_ui_with_response)
        self.request_thread.start()

    def update_ui_with_response(self, response: urllib3.response.HTTPResponse):
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

    def clear_ui_before_request(self):
        self.response_raw.setText('')
        self.app_state.response_attributes.raw_response = ''
        self.app_state.response_attributes.headers = {}
        self.response_headers_table.setRowCount(0)


def bind_actions(rester: Rester):
    rester.request_type.activated[str].connect(rester.on_url_type_changed)
    rester.send_btn.clicked.connect(rester.handle_request_send)


if __name__ == '__main__':
    app_context = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = QtWidgets.QMainWindow()
    rester_main_window = Rester()

    rester_main_window.setupUi(window)
    bind_actions(rester_main_window)

    window.resize(1200, 800)
    window.show()
    exit_code = app_context.app.exec_()  # 2. Invoke app_context.app.exec_()
    sys.exit(exit_code)
