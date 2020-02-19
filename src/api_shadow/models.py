from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ShadowModel(db.Model):
    __tablename__ = 'shadows'

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    soil_ph = db.Column(db.Float(precision=4))
    soil_temp = db.Column(db.Float(precision=4))
    soil_humi = db.Column(db.Float(precision=4))
    air_temp = db.Column(db.Float(precision=4))
    air_humi = db.Column(db.Float(precision=4))
    air_pres = db.Column(db.Float(precision=4))
    alarm_current = db.Column(db.Boolean())
    alarm_desired = db.Column(db.Boolean())
    batt_status = db.Column(db.Integer)

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
    
    time_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    time_updated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

