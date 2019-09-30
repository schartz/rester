import sys
import urllib3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from fbs_runtime.application_context.PyQt5 import ApplicationContext

import models.app_state as app_state
from threads.http import HttpThread
from ui.ui import Ui_mainWindow as ResterUiWindow
from utils import utils


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
        self.app_state.request_attributes.url = self.url.text()
        self.request_thread.request_completed.connect(self.handle_http_response)
        self.progress_bar.setVisible(True)
        self.prepare_request()
        self.request_thread.start()

    def prepare_request(self):
        self.clear_ui_before_request()

        # set up headers
        for row in range(self.request_headers_table.rowCount()):
            key = self.request_headers_table.item(row, 1).text()
            value = self.request_headers_table.item(row, 2).text()
            self.app_state.request_attributes.headers[key] = value

        # set up request URL Parameters
        print()
        for row in range(self.params_table.rowCount()):
            key = self.params_table.item(row, 1).text()
            value = self.params_table.item(row, 2).text()
            self.app_state.request_attributes.parameters[key] = value


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
        delete_button.clicked.connect(self.delete_selected_header)
        delete_button.setStyleSheet("color: red; font-weight: bold")

        self.headers_tab_title.setText('Headers (' + str(insert_position + 1) + ')')

    def add_new_parameter_area(self):
        insert_position = self.params_table.rowCount()
        self.params_table.insertRow(insert_position)

        delete_button = QtWidgets.QPushButton("x")
        self.params_table.setCellWidget(insert_position, 0, delete_button)
        delete_button.clicked.connect(self.delete_selected_param)
        delete_button.setStyleSheet("color: red; font-weight: bold")

        self.params_tab_title.setText('URL Query Parameters (' + str(insert_position + 1) + ')')

    def delete_selected_header(self):
        button = self.main_window.sender()
        if button:
            row = self.request_headers_table.indexAt(button.pos()).row()
            self.request_headers_table.removeRow(row)
            self.headers_tab_title.setText('Headers (' + str(self.request_headers_table.rowCount()) + ')')

    def delete_selected_param(self):
        button = self.main_window.sender()
        if button:
            row = self.params_table.indexAt(button.pos()).row()
            self.params_table.removeRow(row)
            self.params_tab_title.setText('URL Query Parameters (' + str(self.params_table.rowCount()) + ')')

    def set_no_body_request(self):
        self.raw_body_type.setVisible(False)

    def set_form_data_request(self):
        self.raw_body_type.setVisible(False)

    def set_url_encoded_form_data_request(self):
        self.raw_body_type.setVisible(False)

    def set_raw_data_request(self):
        self.raw_body_type.setVisible(True)


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
    rester.add_new_param_btn.clicked.connect(rester.add_new_parameter_area)

    rester.raw_body_type.setVisible(False)
    rester.radio_button_nobody.clicked.connect(rester.set_no_body_request)
    rester.radio_button_form_data.clicked.connect(rester.set_form_data_request)
    rester.radio_button_url_form_data.clicked.connect(rester.set_url_encoded_form_data_request)
    rester.radio_button_raw.clicked.connect(rester.set_raw_data_request)


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
