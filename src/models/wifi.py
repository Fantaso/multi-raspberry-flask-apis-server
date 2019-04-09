from src import db


class Wifi(db.Model):
    __tablename__ = 'wifis'

    id = db.Column(db.Integer, primary_key=True)
    ssid = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    # Device[one]-Wifi[one] 
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    def __init__(self, data):
        self.ssid = data.get('ssid')
        self.password = data.get('password')
        
    def __repr__(self):
        return f'{self.__class__.__name__}(ssid={self.ssid}, password={self.password})'

    def __str__(self):
        return f'<Wifi: {self.ssid}>'
    

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

    @staticmethod
    def get_wifi(id):
        return Wifi.query.get(id)