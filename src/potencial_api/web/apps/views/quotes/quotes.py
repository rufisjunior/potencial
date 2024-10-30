from flask import Blueprint, render_template
from flask_classful import route
from potencial_api.web.api.views.base import Base


app = Blueprint('quote', __name__, template_folder='templates', static_folder='potencial_api.web.apps.views.home.static.content')

class InsuranceQuoteView(Base):
    @route('/calcular', methods=['GET'])
    def quotes_page(self):
        return render_template('quotes.html')
    
InsuranceQuoteView.register(app)