from potencial_api.core.vehicle import Vehicle as VehicleClient
from potencial_api.domain.entities.check_vehicle import CheckVehicle
from potencial_api.domain.entities.vehicle_model import VehicleModel

class VehicleService:
    def __init__(self):
        self.__vehicle_client = VehicleClient()
        self.__model = VehicleModel()


    def process_request(self, plate, path_value):
        
        model = self.__buil_contact(plate)

        response = self.__vehicle_client.get_vehicle(model, path_value)

        return self.__model._convert_vehicle(response)
    
    def erich_vehicle():
        return
    
    def __buil_contact(self, placa):
        checkVehicle = CheckVehicle()

        checkVehicle.campo = 'PLACA'
        checkVehicle.source = 'TELEPORT'
        checkVehicle.estrutura_vendas = '1'
        checkVehicle.valor = placa
        
        return checkVehicle