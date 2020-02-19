from flask_restful import Resource

class DeviceWifiView(Resource):
    def get(self):
        return {'message': 'Hello from DeviceWifiView GET'}

    def post(self):
        return {'message': 'Hello from DeviceWifiView POST'}