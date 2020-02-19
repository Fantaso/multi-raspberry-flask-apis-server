from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()

class TimeSeriesSchema(ma.Schema):
    id = fields.Integer(dump_only=True)


# class marshmallow.fields.Boolean(truthy=None, falsy=None, **kwargs)
# class marshmallow.fields.String(default=<marshmallow.missing>, attribute=None, data_key=None, error=None, validate=None, required=False, allow_none=None, load_only=False, dump_only=False, missing=<marshmallow.missing>, error_messages=None, **metadata)
# class marshmallow.fields.DateTime(format=None, **kwargs)[source]
# class marshmallow.fields.Float(allow_nan=False, as_string=False, **kwargs)