from flask_classful import route
from flask import Blueprint, render_template
from potencial_api.web.api.views.base import Base

app = Blueprint('faq', __name__, template_folder='templates', static_folder='potencial_api.web.apps.views.home.static.content')

class FaqView(Base):

    @route('/faq', methods=['GET'])
    def faq_page(self):
        return render_template('faq.html')
    
FaqView.register(app)