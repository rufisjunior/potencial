

import json
from potencial_api.client.base_client import BaseClient
from potencial_api.settings.core import API_KEY_RD_STATION, CORE_URL_API_RD_STATION


class Tracking(BaseClient):
    def __init__(self, host=CORE_URL_API_RD_STATION, api_key = API_KEY_RD_STATION):
        self.__host = host
        super().__init__()

    @property
    def host(self):
        return self.__host
    
    def build_headers(self):
        return {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    
    def create_tracking(self, model):
        path = '/platform/conversions'
        params = {'api_key': API_KEY_RD_STATION}
        body = json.dumps(model)

        response = self.post(path, body, query_params=params)
        return response.content

    
    def post(self, path, body=None, query_params=None, extra_headers=None):
        try:
            return super().post(path=path, body=body, query_params=query_params, extra_headers=extra_headers) 
        except Exception as error:
            raise Exception('Object not found', error)

