import json
import xmltodict
from potencial_api.core.address import Address as AddressClient


class AddressService:
    def __init__(self):
        self.__address_client = AddressClient()

    def process_request(self, cep):
        response = self.__address_client.get_address(cep)

        return self.convert_to_json(response)
    
    def convert_to_json(self, response):
        return self.abstract_value(response)


        
    

    def abstract_value(self, value):
        data_dict = xmltodict.parse(value)

        return json.dumps(data_dict)