import sys
import urllib3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from fbs_runtime.application_context.PyQt5 import ApplicationContext

import src.main.python.models.app_state as app_state
from src.main.python.threads.http import HttpThread
from src.main.python.ui.ui import Ui_mainWindow as ResterUiWindow
from src.main.python.utils import utils


class Rester(ResterUiWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.app_state = app_state.AppState()
        self.http_client = urllib3.PoolManager()
        self.request_thread = HttpThread(self.app_state.request_attributes)
        self.message_box = QMessageBox()

    def on_url_type_changed(self, text: str) -> None:
        self.app_state.request_attributes.request_type = text

    def send_request(self):
        self.clear_ui_before_request()
        self.app_state.request_attributes.url = self.url.text()
        self.request_thread.request_completed.connect(self.handle_http_response)
        self.progress_bar.setVisible(True)
        self.request_thread.start()

    def handle_http_response(self, response_signal: dict):
        self.progress_bar.setVisible(False)
        if not response_signal.get('is_success'):
            print(response_signal.get('error'))

            self.message_box.setIcon(QMessageBox.Critical)
            self.message_box.setText("Error")
            self.message_box.setInformativeText(response_signal.get('error'))
            self.message_box.setWindowTitle("Error")
            self.message_box.exec_()
            return

        response = response_signal.get('response')

        raw_response = str(response.data)

        headers = response.headers
        # print(headers)
        # print(utils.get_charset(headers))
        self.response_headers_table.setRowCount(len(headers))
        i = 0
        for key in headers:
            self.response_headers_table.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            self.response_headers_table.setItem(i, 1, QtWidgets.QTableWidgetItem(headers[key]))
            i += 1
        self.progress_bar.setVisible(False)

        self.app_state.response_attributes.text_response = response.data.decode(utils.get_charset(headers))
        self.app_state.response_attributes.headers = headers

        self.pretty_view.setText(self.app_state.response_attributes.text_response)
        self.response_raw.setText(raw_response)
        self.app_state.response_attributes.raw_response = raw_response
        self.response_status.setText('Response Status Code: ' + str(response.status))
        if str(response.status).startswith('2'):
            self.response_status.setStyleSheet('color: green')
        elif str(response.status).startswith('3'):
            self.response_status.setStyleSheet('color: orange')
        else:
            self.response_status.setStyleSheet('color: red')
        self.response_status.setVisible(True)

    def clear_ui_before_request(self):
        self.response_raw.setText('')
        self.app_state.response_attributes.raw_response = ''
        self.app_state.response_attributes.headers = {}
        self.response_headers_table.setRowCount(0)
        self.response_status.setVisible(False)
        self.pretty_view.setText('')

    def add_new_header_area(self):
        insert_position = self.request_headers_table.rowCount()
        self.request_headers_table.insertRow(insert_position)

        delete_button = QtWidgets.QPushButton("x")
        self.request_headers_table.setCellWidget(insert_position, 0, delete_button)
        delete_button.clicked.connect(self.delete_selected_row)
        delete_button.setStyleSheet("color: red; font-weight: bold")
        delete_button.setGeometry(20, 30, 20, 30)

        self.headers_tab_title.setText('Headers(' + str(insert_position + 1) + ')')

    def delete_selected_row(self):
        button = self.main_window.sender()
        if button:
            row = self.request_headers_table.indexAt(button.pos()).row()
            self.request_headers_table.removeRow(row)
            self.headers_tab_title.setText('Headers(' + str(self.request_headers_table.rowCount()) + ')')


def bind_actions(rester: Rester):
    rester.req_res_container_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    rester.req_container_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    rester.res_container_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    rester.response_headers_table.setAlternatingRowColors(True)

    rester.progress_bar.setVisible(False)
    rester.response_status.setVisible(False)

    rester.request_type.activated[str].connect(rester.on_url_type_changed)
    rester.send_btn.clicked.connect(rester.send_request)
    rester.add_new_header_btn.clicked.connect(rester.add_new_header_area)


if __name__ == '__main__':
    # Instantiate ApplicationContext
    app_context = ApplicationContext()
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    rester_main_window = Rester(window)
    rester_main_window.setupUi(window)
    bind_actions(rester_main_window)
    window.resize(1200, 800)
    app.setStyle(QtWidgets.QStyleFactory.create('WindowsXP'))
    print(QtWidgets.QStyleFactory.keys())
    window.show()

    # Invoke app_context.app.exec_()
    exit_code = app_context.app.exec_()
    sys.exit(exit_code)
