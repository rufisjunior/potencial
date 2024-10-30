
      
from flask import Blueprint, jsonify, request
from flask_classful import route
from potencial_api.domain.services.insurance_quote_service import InsuranceQuoteService
from potencial_api.web.api.views.base import Base


app = Blueprint('insurance-quote', __name__)

class InsuranceQuoteView(Base):
    def __init__(self):
        self.__quote_service = InsuranceQuoteService()
    
    @route('/cotar', methods=['POST'])
    def insurance_quote(self):
        try:
            data = request.data

            return self.__quote_service.process_request(data)

        except Exception as error:
            return jsonify({'error': f'Erro: {error}'}) 
        
    @route('/person', methods=['POST'])
    def insurance_person(self):
        try:
            data = request.data

            response = self.__quote_service.get_person_request(data)
            return jsonify(response.__dict__)

        except Exception as error:
            return jsonify({'error': f'Erro: {error}'}) 
        
    @route('/tracking', methods=['POST'])
    def insurance_marketing(self):
        try:
            data = request.data

            response = self.__quote_service.post_tracking_lead(data)

            return response

        except Exception as error:
            return jsonify({'error': f'Erro: {error}'}) 



InsuranceQuoteView.register(app)