import json

from flask import Flask, request
from flask_cors import CORS
from flask_log_request_id import RequestID, current_request_id


class BootstrapFlaskApplication:
    def __init__(self):
        self.application = Flask('potencia_api')

    def __call__(self):
        #self.__configure_flask_application_cors()
        #self.__configure_flask_application_request_id()

        return self.application

    def __configure_flask_application_cors(self):
        CORS(self.application)
        RequestID(self.application)

    def __configure_flask_application_request_id(self):
        @self.application.after_request
        def append_request_id(response):
            response.headers.add('X-REQUEST-ID', current_request_id())

            data = request.get_data()
            try:
                data = json.loads(data.decode('utf-8'))
            except Exception:
                pass

            user_agent = request.headers.get('User-Agent')
            remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

            print(user_agent)
            print(remote_addr)


            return response
