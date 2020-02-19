from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class ShadowSchema(ma.Schema):
    id = fields.Integer(dump_only=True)

    # User Shadow
    mac = fields.String(dump_only=True)
    ip_address = fields.String(dump_only=True)
    username = fields.String(dump_only=True)
    # password = fields.String()

    # MeasurementShadow
    timestamp = fields.DateTime(dump_only=True)
    soil_ph = fields.Float(dump_only=True)
    soil_temp = fields.Float(dump_only=True)
    soil_humi = fields.Float(dump_only=True)
    air_temp = fields.Float(dump_only=True)
    air_humi = fields.Float(dump_only=True)
    air_pres = fields.Float(dump_only=True)
    batt_status = fields.Integer(dump_only=True)

    alarm_current = fields.Boolean(dump_only=True)
    alarm_desired = fields.Boolean()

    # Threshold Shadow
    soil_ph_min = fields.Float()
    soil_ph_max = fields.Float()
    soil_temp_min = fields.Float()
    soil_temp_max = fields.Float()
    soil_humi_min = fields.Float()
    soil_humi_max = fields.Float()
    air_temp_min = fields.Float()
    air_temp_max = fields.Float()
    air_humi_min = fields.Float()
    air_humi_max = fields.Float()
    air_pres_min = fields.Float()
    air_pres_max = fields.Float()
    
    time_created = fields.DateTime(dump_only=True)
    time_updated = fields.DateTime(dump_only=True)


# class marshmallow.fields.Boolean(truthy=None, falsy=None, **kwargs)
# class marshmallow.fields.String(default=<marshmallow.missing>, attribute=None, data_key=None, error=None, validate=None, required=False, allow_none=None, load_only=False, dump_only=False, missing=<marshmallow.missing>, error_messages=None, **metadata)
# class marshmallow.fields.DateTime(format=None, **kwargs)[source]
# class marshmallow.fields.Float(allow_nan=False, as_string=False, **kwargs)