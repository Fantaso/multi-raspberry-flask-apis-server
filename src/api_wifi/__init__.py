from flask import Blueprint
from flask_restful import Api
from .views import DeviceWifiView

api_bp_wifi = Blueprint('api_bp_wifi', __name__)
api = Api(api_bp_wifi)

api.add_resource(DeviceWifiView, '/')