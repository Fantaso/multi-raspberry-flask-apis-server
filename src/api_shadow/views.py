from flask_restful import Resource


class ShadowStatusView(Resource):
    def get(self):
        return {'message': 'This is the ShadowStatusView GET'}


class ShadowUpdateView(Resource):
    def put(self):
        return {'message': 'This is the ShadowUpdateView PUT'}

    def patch(self):
        return {'message': 'This is the ShadowUpdateView PATCH'}