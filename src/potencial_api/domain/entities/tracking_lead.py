import json


class TrackingLead:
    def __init__(self):
        self.email: str
        self.name: str
        self.mobile_phone: str
       

    def _convert_tracking_lead(self, data):
        track = TrackingLead()

        datas =  json.loads(data)

        track.email = datas['email']
        track.name = datas['name']
        track.mobile_phone = datas['phone']

        return {
            "event_type": 'CONVERSION',
            "event_family": 'CDP',
            "payload" : {
                "conversion_identifier":'Campanha google inicial',
                "email": track.email,
                "name": track.name,
                "mobile_phone": track.mobile_phone
            }    
        }