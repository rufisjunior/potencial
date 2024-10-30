from flask import Blueprint
from flask import jsonify, request
from flask_classful import route
from potencial_api.domain.services.vehicle_service import VehicleService
from potencial_api.settings.core import CORE_PATH_AUTO_COMPLETE

from potencial_api.web.api.views.base import Base

app = Blueprint('vehicle', __name__)

class VehicleView(Base):
    def __init__(self):
        self.__vehicle_service = VehicleService()
           
    @route('/vehicle/auto-complete/placa', methods=['GET'])
    def vehicle_auto_complete(self, path_auto_complete=CORE_PATH_AUTO_COMPLETE):
        path_auto_complete = path_auto_complete

        try:
            plate = request.args['placa']
        
            response = self.__vehicle_service.process_request(plate, path_auto_complete)

            return jsonify(response.__dict__)
        
        except Exception as error:
            return jsonify({'error': f'Erro: {error}'})
    
VehicleView.register(app)