import requests

from abc import ABC, abstractmethod
from requests import Request
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout

from potencial_api.settings.core import TIMEOUT



class BaseClient(ABC):
    def __init__(self, timeout=TIMEOUT):
        self.timeout = timeout or int(100)

    
    @property
    @abstractmethod
    def host(self):
        pass

    @abstractmethod
    def build_headers(self):
        pass

    def get(self, path, body=None, query_params=None, extra_headers=None):
        headers = extra_headers or {}
        return self.perform_request('get', path,body=body, query_params=query_params, extra_headers=headers)
    
    def post(self, path, body, query_params=None, extra_headers=None):
        headers = extra_headers or {}
        return self.perform_request('post', path=path, body=body, query_params=query_params,extra_headers=headers)
    
    def perform_request(self, method, path, body, json=None, query_params=None, extra_headers=None):
        url = f'{self.host}{path}' if not path.startswith('http') else path
        headers = {**self.build_headers(), **extra_headers}

        try:
            response = requests.request(
                method=method,
                url=url,
                data=body,
                params=query_params,
                headers=headers,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response
        except (ConnectionError, ConnectTimeout) as error:
            raise error
        
        except HTTPError as error:
            raise error