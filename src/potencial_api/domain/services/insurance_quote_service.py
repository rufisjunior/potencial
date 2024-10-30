
import dicttoxml
import json
from potencial_api.core.insurance_quote import InsuranceQuote as InsuranceQuoteClient
from potencial_api.core.tracking import Tracking as TrackingClient
from potencial_api.core.vehicle import Vehicle
from potencial_api.domain.entities.check_person import CheckPerson
from potencial_api.domain.entities.person_model import PersonModel
from potencial_api.domain.entities.tracking_lead import TrackingLead


class InsuranceQuoteService:
    def __init__(self):
        self.__insurance_quote = InsuranceQuoteClient()
        self.__insurance_tracking = TrackingClient()
        self.__insurance_person = Vehicle()
        self.__convert_person = PersonModel()
        self.__params = CheckPerson()
        self.__tracking = TrackingLead()

    def process_request(self, data):
        model = self.build_body(data)

        result = self.__insurance_quote.post_quote(model)
        return result
    
    def get_person_request(self, data):
        model = self.__build_contact(data)

        response = self.__insurance_person.get_person(model)
        return self.__convert_person._convert(response)
    
    def post_tracking_lead(self, data):
        model = self.__build_tracking(data)

        response = self.__insurance_tracking.create_tracking(model)
        return response

    

    def build_body(self, data):
        convert_json = json.loads(data)

        model = dicttoxml.dicttoxml(convert_json, root=False, xml_declaration=False, attr_type=False)
        return model
    
    def __build_contact(self, data):
        return self.__params._convert_params_person(data)
    
    def __build_tracking(self, data):
        return self.__tracking._convert_tracking_lead(data)
