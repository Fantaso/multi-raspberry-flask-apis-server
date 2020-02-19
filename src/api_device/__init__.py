from flask import Blueprint
from flask_restful import Api
from .views import DeviceCheckView, DeviceRegisterView, DeviceDeregisterView

api_bp_device = Blueprint('api_bp_device', __name__)
api = Api(api_bp_device)

api.add_resource(DeviceCheckView, '/')
api.add_resource(DeviceRegisterView, '/register')
api.add_resource(DeviceDeregisterView, '/deregister')