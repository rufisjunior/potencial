
from potencial_api.core.profession import Profession as ProfessionClient

class ProfessionService:
    def __init__(self):
        self.__profession_client = ProfessionClient()

    def process_request(self):
        return self.__profession_client.get_profession()