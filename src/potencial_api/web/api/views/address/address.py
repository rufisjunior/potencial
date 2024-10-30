from flask import jsonify, request
from flask import Blueprint
from flask_classful import route
from potencial_api.domain.services.address_service import AddressService


from potencial_api.web.api.views.base import Base

app = Blueprint('address', __name__)

class AddressView(Base):
    def __init__(self):
        self.__addressService = AddressService()

    @route('/address/cep', methods=['GET'])
    def address(self):
        try:
            cep = request.args['cep']

            return self.__addressService.process_request(cep)

        except Exception as error:
            return jsonify({'error': f'Erro: {error}'})


AddressView.register(app)