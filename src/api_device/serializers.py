from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

from src.device.models import Device


ma = Marshmallow()


class DeviceSchema(ma.Schema):
    # class Meta:
    #     model = Device

    id = fields.Integer(dump_only=True)
    mac = fields.String(dump_only=True)
    ip_adr = fields.String(dump_only=True)
    mac_adr = fields.String(dump_only=True)

    client_ip_adr = fields.String(required=True)
    username = fields.String(required =True)
    password = fields.String(required =True)
    
    time_created = fields.DateTime(dump_only=True)
    time_updated = fields.DateTime(dump_only=True)

# validate=validate.Length(1)
# class marshmallow.fields.Boolean(truthy=None, falsy=None, **kwargs)
# class marshmallow.fields.String(default=<marshmallow.missing>, attribute=None, data_key=None, error=None, validate=None, required=False, allow_none=None, load_only=False, dump_only=False, missing=<marshmallow.missing>, error_messages=None, **metadata)
# class marshmallow.fields.DateTime(format=None, **kwargs)[source]
# class marshmallow.fields.Float(allow_nan=False, as_string=False, **kwargs)