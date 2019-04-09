from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.config import app_config


# init core services
db = SQLAlchemy()
migrate = Migrate()

def create_app(app_env):
    app = Flask(__name__)
    app.config.from_object(app_config[app_env])

    db.init_app(app)
    migrate.init_app(app, db)

    from src.api_wifi import api_bp_wifi
    from src.api_device import api_bp_device
    from src.api_shadow import api_bp_shadow
    from src.api_timeseries import api_bp_timeseries
    app.register_blueprint(api_bp_wifi, url_prefix='/wifi')
    app.register_blueprint(api_bp_device, url_prefix='/device')
    app.register_blueprint(api_bp_shadow, url_prefix='/shadow')
    app.register_blueprint(api_bp_timeseries, url_prefix='/timeseries')

    @app.route('/')
    def index():
        """You are at Index RaspberryPI API."""
        return jsonify({'message':'You are at Index RaspberryPI API.'})

    return app