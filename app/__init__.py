from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootsrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # create app configs
    app.config.from_object
    (config_options[config_name])
    config_options[config_name].init_app(app)

    # reg a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    
