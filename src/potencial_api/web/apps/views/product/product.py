from flask import Blueprint, render_template
from flask_classful import route
from potencial_api.web.api.views.base import Base


app = Blueprint('product', __name__, template_folder='templates', static_folder='potencial_api.web.apps.views.home.static.content')

class ProductView(Base):

    @route('/produtos', methods=['GET'])
    def product_page(self):
        return render_template('product.html')
    
ProductView.register(app)