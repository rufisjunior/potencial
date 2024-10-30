
from potencial_api.settings.core import API_KEY, CODE_CORRECTOR, CORE_URL_TELEPORT, PASSWORD_CORRECTOR, PASSWORD_TELEPORT, PATH_TELEPORT

from potencial_api.client.base_client import BaseClient


class InsuranceQuote(BaseClient):
    def __init__(self, host=CORE_URL_TELEPORT, api_key=API_KEY):
        self.__host = host
        super().__init__()

    
    @property
    def host(self):
        return self.__host
    
    def build_headers(self):
        return {
            'X-API-KEY': API_KEY,
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'urn:uTeleport-Teleport#GravarCalculo'
        }
    
    def post_quote(self, model):
        path = PATH_TELEPORT
        body = self.body_config(model)

        response = self.post(path, body)

        return response.content

    def body_config(self, model, password=PASSWORD_TELEPORT, codeCorr=CODE_CORRECTOR, passwordCorr=PASSWORD_CORRECTOR):
         return f'''<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                            <soap:Body>
                                <GravarCalculo xmlns="http://teleport.com.br/">
                                    <senha>{password}</senha>
                                    <CodCorr>{codeCorr}</CodCorr>
                                    <SenhaCorr>{passwordCorr}</SenhaCorr>
                                    <XML>{model}</XML>
                                </GravarCalculo>
                            </soap:Body>
                        </soap:Envelope>'''
    

        
    def post(self, path, body=None, query_params=None, extra_headers=None):
        try:
            return super().post(path=path, body=body, query_params=query_params, extra_headers=extra_headers) 
        except Exception as error:
            raise Exception('Object not found', error)