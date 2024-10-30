
from autodiscover import AutoDiscover
from pathlib import Path
from potencial_api.web.api import api
from potencial_api.web.apps import apps
from potencial_api.web import BootstrapFlaskApplication


API_PATH = Path('potencial_api/web/api/views')
APPS_PATH = Path('potencial_api/web/apps/views')



class App():

    def start(self):
        self.app = self.__initialize_application()
        self.__register_apis()
        self.__inject_blueprint(self.app)
        return self.app

    
    def __register_apis(self):
        AutoDiscover(API_PATH)()
        AutoDiscover(APPS_PATH)()

        self.app.register_blueprint(api)
        self.app.register_blueprint(apps)

    def __inject_blueprint(self, app):
        from .web.api.views.vehicle.vehicle import app as app_vehicle
        from .web.api.views.address.address import app as app_address
        from .web.api.views.profession.profession import app as app_profession
        from .web.api.views.insurance_quote.insurance_quote import app as app_insurance_quote

        
        from .web.apps.views.home.index import app as app_home
        from .web.apps.views.quotes.quotes import app as app_quote
        from .web.apps.views.insurers.insurers import app as app_insurers
        from .web.apps.views.product.product import app as app_product
        from .web.apps.views.faq.faq import app as app_faq

        app.register_blueprint(app_insurance_quote)
        app.register_blueprint(app_vehicle)
        app.register_blueprint(app_address)
        app.register_blueprint(app_profession)
        app.register_blueprint(app_home)
        app.register_blueprint(app_quote)
        app.register_blueprint(app_insurers)
        app.register_blueprint(app_product)
        app.register_blueprint(app_faq)

    def __initialize_application(self):
        app = BootstrapFlaskApplication()()

        return app
       
app = App()