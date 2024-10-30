from flask_classful import FlaskView

class Base(FlaskView):
    route_base = '/'
    roles = ['api-client']