class AppState:
    def __init__(self):
        self.initialized = 0
        self.completed = 0
        self.request_attributes = RequestAttributes()
        self.response_attributes = ResponseAttributes()


class RequestAttributes:
    def __init__(self):
        self.request_type = 'get'
        self.url = 'url'
        self.parameters = {}
        self.authorization = {'type': 'noauth', 'token': ''}
        self.headers = {}
        self.body = ''


class ResponseAttributes:
    def __init__(self):
        self.status_code = 0
        self.raw_response = ''
        self.text_response = ''
        self.headers = {}
