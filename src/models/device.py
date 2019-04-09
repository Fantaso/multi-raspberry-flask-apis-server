from src import db


class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    mac_addr = db.Column(db.String(50), unique=True, nullable=False)
    netmask = db.Column(db.String(50), nullable=False)
    ip_addr = db.Column(db.String(50), nullable=False)

    # client information
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    client_ip_addr = db.Column(db.String(50))
    
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    # Device[one]-Threshold[one] 
    threshold = db.relationship('Threshold', uselist=False, backref='device', lazy='joined')
    # Device[one]-Threshold[one] 
    wifi = db.relationship('Wifi', uselist=False, backref='device', lazy='joined')
    # Device[one]-Measurements[many]
    measurements = db.relationship('Measurement', backref='device', lazy='dynamic')

    def __init__(self, data):
        self.mac_addr = data.get('mac_addr')
        self.ip_addr = data.get('ip_addr')
        self.netmask = data.get('netmask')
        self.username = data.get('username')
        self.password = data.get('password')
        self.client_ip_addr = data.get('client_ip_addr')
        self.threshold = data.get('threshold')
        # self.measurements = data.get('measurements')
    
    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'<Device: {self.ip_addr}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for k, v in data.items():
            # if k == 'measurements':
            #     getattr(self, k).extend(v)
            #     continue
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_device(id):
        return Device.query.get(id)