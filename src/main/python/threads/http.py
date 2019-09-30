from PyQt5 import QtCore
import urllib3
from models.app_state import RequestAttributes
from urllib.parse import urlencode, quote_plus


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
            print(req.headers)
            print(req.parameters)

            if req.request_type == 'GET' or req.request_type == 'HEAD' or req.request_type == 'DELETE':
                # For GET, HEAD, and DELETE requests, you can simply pass the arguments
                # as a dictionary in the fields argument to request()
                response = self.http_client.request(method=req.request_type, url=req.url, headers=req.headers, fields=req.parameters)
                self.request_completed.emit(
                    {'is_success': True, 'response': response, 'error': None, 'status_message': response.status})

            if req.request_type == 'POST' or req.request_type == 'PUT' or req.request_type == 'PATCH':
                # For POST and PUT requests, you need to manually encode query parameters in the URL:
                url_encoded_args = urlencode(req.parameters, quote_via=quote_plus)
                url = req.url + '?' + url_encoded_args
                response = self.http_client.request(method=req.request_type, url=url, headers=req.headers,
                                                    fields=req.parameters)
                self.request_completed.emit(
                    {'is_success': True, 'response': response, 'error': None, 'status_message': response.status})

        except Exception as e:
            self.request_completed.emit({'is_success': False, 'response': None, 'error': str(e)})



