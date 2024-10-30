

from potencial_api.client.base_client import BaseClient
from potencial_api.settings.core import API_KEY, CORE_URL_TELEPORT, PASSWORD_TELEPORT, PATH_TELEPORT


class Address(BaseClient):
    def __init__(self, host=CORE_URL_TELEPORT, api_key=API_KEY):
        self.__host = host
        super().__init__()     

    @property
    def host(self):
        return self.__host   
        
    def build_headers(self):
        return{
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'urn:uTeleport-Teleport#ConsultaCEP',
            'X-API-KEY': API_KEY
        }
    
    def get_address(self, cep:str):
        
        body = self.build_body(cep)
        path = PATH_TELEPORT

        response = self.post(path, body)

        return response.content


    def build_body(self, cep:str, password=PASSWORD_TELEPORT):
        return  f'''<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                            <soap:Body>
                                <ConsultaCEP>
                                    <senha>{password}</senha>
                                    <CEP>{cep}</CEP>
                                </ConsultaCEP>
                            </soap:Body>
                        </soap:Envelope>'''
    
    
    def post(self, path, body, query_params=None, extra_headers=None):
        try:
            return super().post(path, body, query_params, extra_headers)
        except Exception as error:
            raise Exception('Object not found', error)
    