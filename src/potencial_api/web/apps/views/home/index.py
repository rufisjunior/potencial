from flask import Blueprint, render_template
from flask_classful import route
from potencial_api.web.api.views.base import Base

app = Blueprint('home', __name__, template_folder='templates', static_folder='static/content')

class HomeView(Base):

    @route('/', methods=['GET'])
    def home_page(self):
        return render_template('index.html')
    
HomeView.register(app)