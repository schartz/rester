from PyQt5 import QtCore
import urllib3
from src.main.python.models.app_state import RequestAttributes


class HttpThread(QtCore.QThread):

    request_completed = QtCore.pyqtSignal(dict)

    def __init__(self, request_attributes: RequestAttributes):
        QtCore.QThread.__init__(self)
        self.request_attributes = request_attributes
        self.http_client = urllib3.PoolManager()

    def __del__(self):
        self.wait()

    def run(self) -> None:
        return self._execute_http_request(self.request_attributes)

    def _execute_http_request(self, req: RequestAttributes):
        try:
            response = self.http_client.request(method=req.request_type, url=req.url, fields=req.headers)
            self.request_completed.emit({'is_success': True, 'response': response, 'error': None, 'status_message': response.status})
        except Exception as e:
            self.request_completed.emit({'is_success': False, 'response': None, 'error': str(e)})



