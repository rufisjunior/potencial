
import pickle
import json


class VehicleModel:
    def __init__(self):
        self.CODCAR: str
        self.MARCA : str
        self.ANOFABR: str
        self.ANOMODELO: str
        self.COMBUSTIVEL: str
        self.PLACANUM : str
        self.CAMBIOAUTO: str
        self.DESCRICAO: str
        self.CHASSI: str

    def _convert_vehicle(self, vehicle_data):
        vehicle = VehicleModel()

        if vehicle_data is None:
            return vehicle
        
       

        fuel = vehicle_data['combustivel']
        fipe = vehicle_data['fipe']
        
        if(fipe is not None):
            for item in fipe:

                teleport_data = item['teleport_data']

                for itens in teleport_data:
                    vehicle.CODCAR = itens['cod_car']

               

        vehicle.DESCRICAO = vehicle_data['modelo']
        vehicle.MARCA = vehicle_data['marca']
        vehicle.ANOFABR = vehicle_data['ano_fabricacao']
        vehicle.ANOMODELO = vehicle_data['ano_modelo']
        vehicle.PLACANUM = vehicle_data['placa']
        vehicle.CAMBIOAUTO = vehicle.DESCRICAO.__contains__('AUT')
        vehicle.CHASSI = vehicle_data['chassi']
        vehicle.COMBUSTIVEL = self.__combustivel(fuel)

        return vehicle
    
    def __combustivel(self, typeFuel):

        if typeFuel == "Gasolina":
            return "1"
        elif typeFuel == "Álcool":
            return "2"
        elif typeFuel == "Diesel":
            return "3"
        elif typeFuel == "Elétrico":
            return "4"
        elif typeFuel == "ALCOOL / GASOLINA":
            return "5"
        elif typeFuel == "Gasolina / Adaptado a gás":
            return "6"
        elif typeFuel == "Alcooç / Adaptado a gás":
            return "7"
        elif typeFuel == "Outros":
            return "12"

