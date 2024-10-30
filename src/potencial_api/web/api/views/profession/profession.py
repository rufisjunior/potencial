from flask_classful import route
from flask import Blueprint, jsonify
from potencial_api.domain.services.profession_service import ProfessionService
from potencial_api.web.api.views.base import Base


app = Blueprint('profession', __name__)

class ProfessionView(Base):
    def __init__(self):
        self.__profession_service = ProfessionService()

    @route('/profession', methods=['GET'])
    def profession(self):

        try:
            response = self.__profession_service.process_request()

            return response

        except Exception as error:
            return jsonify({'error': f'{error} - {response.text}'})
                           
ProfessionView.register(app)