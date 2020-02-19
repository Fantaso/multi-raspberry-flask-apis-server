from flask_restful import Resource


class TimeSeriesOneView(Resource):
    def get(self):
        return {'message': 'Message from TimeSeriesOneView - GET - last measurement'}


class TimeSeriesTenView(Resource):
    def get(self):
        return {'message': 'Message from TimeSeriesTenView - GET - 10 last measurements'}


class TimeSeriesHundredView(Resource):
    def get(self):
        return {'message': 'Message from TimeSeriesHundredView - GET - 100 last measurements'}