from flask import Blueprint, render_template
from flask_classful import route
from potencial_api.web.api.views.base import Base


app = Blueprint('insurers', __name__, template_folder='templates', static_folder='potencial_api.web.apps.views.home.static.content')

class InsurersView(Base):
    @route('/seguradoras', methods=['GET'])
    def insurers_page(self):
        return render_template('insurers.html')
    
InsurersView.register(app)