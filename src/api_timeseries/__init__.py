from flask import Blueprint
from flask_restful import Api
from .views import TimeSeriesOneView, TimeSeriesTenView, TimeSeriesHundredView

api_bp_timeseries = Blueprint('api_bp_timeseries', __name__)
api = Api(api_bp_timeseries)


api.add_resource(TimeSeriesOneView, '/')
api.add_resource(TimeSeriesTenView, '/last-10')
api.add_resource(TimeSeriesHundredView, '/last-100')