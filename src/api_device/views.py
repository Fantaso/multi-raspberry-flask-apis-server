from flask_restful import Resource

class DeviceCheckView(Resource):
    def get(self):
        return {'message': 'I am a RaspberryPi Sensor'}

class DeviceRegisterView(Resource):
    def get(self):
        return {'message': 'Hello from DeviceRegisterView GET'}

    def post(self):
        return {'message': 'Hello from DeviceRegisterView POST'}

class DeviceDeregisterView(Resource):
    def post(self):
        return {'message': 'Hello from DeviceDeregisterView POST'}