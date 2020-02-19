from flask import Blueprint
from flask_restful import Api
from .views import ShadowStatusView, ShadowUpdateView

api_bp_shadow = Blueprint('api_bp_shadow', __name__)

api = Api(api_bp_shadow)
api.add_resource(ShadowStatusView, '/')
api.add_resource(ShadowUpdateView, '/update')