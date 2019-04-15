from src import db


class Measurement(db.Model):
    __tablename__ = 'measurements'

    id = db.Column(db.Integer, primary_key=True)

    soil_ph = db.Column(db.Float(precision=4))
    soil_temp = db.Column(db.Float(precision=4))
    soil_humi = db.Column(db.Float(precision=4))

    air_temp = db.Column(db.Float(precision=4))
    air_humi = db.Column(db.Float(precision=4))
    air_pres = db.Column(db.Float(precision=4))

    alarm_status = db.Column(db.Boolean())

    batt_status = db.Column(db.Integer)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    # Device[one]-Measurements[many]
    # backref = device
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    def __init__(self, data):
        self.soil_ph = data.get('soil_ph')
        self.soil_temp = data.get('soil_temp')
        self.soil_humi = data.get('soil_humi')
        self.air_temp = data.get('air_temp')
        self.air_humi = data.get('air_humi')
        self.air_pres = data.get('air_pres')
        self.alarm_status = data.get('alarm_status')
        self.batt_status = data.get('batt_status')
        self.timestamp = data.get('timestamp')
        # self.device_id = data.get('device_id')

    def __repr__(self):
    		return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'<Measurement at: {self.timestamp}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def latest(self):
        latest = Measurement.query.order_by('-timestamp').first()
        if not latest:
            return {'message': 'No measurements yet'}
        return latest

    @staticmethod
    def last(self, number):
        measurements = Measurement.query.order_by('-timestamp').all().limit(number)
        if not measurements:
            return {'message': 'No measurements yet'}
        return measurements
