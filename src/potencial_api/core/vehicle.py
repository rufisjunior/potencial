

from potencial_api.client.base_client import BaseClient
from potencial_api.domain.entities import check_person, check_vehicle
from potencial_api.settings.core import API_KEY, CORE_PATH_PERSON, CORE_URL_API


class Vehicle(BaseClient):
    def __init__(self, host=CORE_URL_API, api_key=API_KEY):
        self.__host = host
        super().__init__()

    @property
    def host(self):
        return self.__host
    
    def build_headers(self):
        return {
            'X-API-KEY': API_KEY,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br'
        }
    
    def get_vehicle(self, model: check_vehicle, path_value):

        params = self.build_params(model)
        path = path_value

        return self.get(path, query_params=params).json()
    
    def get_person(self, model: check_person):
        params = self.build_params_person(model)
        path = CORE_PATH_PERSON

        return self.get(path, query_params=params).json()
    
    def build_params(self, model: check_vehicle):
        return {
            'campo': model.campo,
            'estrutura_vendas': model.estrutura_vendas,
            'source': model.source,
            'valor': model.valor
        }
    
    def build_params_person(self, model: check_person):
        return {
            'cpf_cnpj': model.cpf_cnpj,
            'estrutura_vendas': model.estrutura_vendas,
            'source': model.source,
            'tipo_pessoa': model.tipo_pessoa
        }

    
    def get(self, path, body=None, query_params=None, extra_headers=None):
        try:
            return super().get(path=path, body=body, query_params=query_params, extra_headers=extra_headers) 
        except Exception as error:
            raise Exception('Object not found', error)