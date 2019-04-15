from src import db
    

class Threshold(db.Model):
    __tablename__ = 'thresholds'

    id = db.Column(db.Integer, primary_key=True)

    soil_ph_min = db.Column(db.Float(precision=4))
    soil_ph_max = db.Column(db.Float(precision=4))
    soil_temp_min = db.Column(db.Float(precision=4))
    soil_temp_max = db.Column(db.Float(precision=4))
    soil_humi_min = db.Column(db.Float(precision=4))
    soil_humi_max = db.Column(db.Float(precision=4))

    air_temp_min = db.Column(db.Float(precision=4))
    air_temp_max = db.Column(db.Float(precision=4))
    air_humi_min = db.Column(db.Float(precision=4))
    air_humi_max = db.Column(db.Float(precision=4))
    air_pres_min = db.Column(db.Float(precision=4))
    air_pres_max = db.Column(db.Float(precision=4))

    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    # Device[one]-Threslhold[one]
    # backref = device
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    
    def __init__(self, data):
        self.soil_ph_min = data.get('soil_ph_min')
        self.soil_ph_max = data.get('soil_ph_max')
        self.soil_temp_min = data.get('soil_temp_min')
        self.soil_temp_max = data.get('soil_temp_max')
        self.soil_humi_min = data.get('soil_humi_min')
        self.soil_humi_max = data.get('soil_humi_max')
        self.air_temp_min = data.get('air_temp_min')
        self.air_temp_max = data.get('air_temp_max')
        self.air_humi_min = data.get('air_humi_min')
        self.air_humi_max = data.get('air_humi_max')
        self.air_pres_min = data.get('air_pres_min')
        self.air_pres_max = data.get('air_pres_max')
        # self.device_id = data.get('device_id')

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'<Threshold: {self.id}>'


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def restore(self):
        from utils.default import threshold_data
        self.update(threshold_data)
        return 'restored'
