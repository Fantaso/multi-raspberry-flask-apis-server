from src import create_app
from src import db

from src.models.wifi import Wifi
from src.models.device import Device
from src.models.threshold import Threshold
from src.models.measurement import Measurement

from .network_setup import NetworkSetUp
from .default_data import threshold_data, wifi_data, measurement_data

class DatabaseSetUp():
    """Set up the initial boot up of the Raspberry Pi Sensor."""
    def __init__(self, app_env = 'development', *args, **kwargs):
        self.db = db
        self.app = create_app(app_env)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.setup_rpi()

    def init_db(self):
        self.db.create_all()

    def get_or_create_threshold(self):
        threshold = Threshold.query.first()
        if not threshold:
            threshold = Threshold(threshold_data)
            threshold.save()
        return threshold

    def get_or_create_wifi(self):
        wifi = Wifi.query.first()
        if not wifi:
            wifi = Wifi(wifi_data)
            wifi.save()
        return wifi

    def get_or_create_measurement(self):
        measurement = Measurement.query.first()
        if not measurement:
            measurement = Measurement(measurement_data)
            measurement.save()
        return measurement

            
    def get_or_create_device(self):
        device = Device.query.first()
        if not device:
            # get data, if get_network_info(not spcify name, gets the first wlan)
            network = NetworkSetUp()
            ip_addr, netmask, mac_addr = network.get_network_info()
            data = {'mac_addr':mac_addr, 'netmask':netmask, 'ip_addr':ip_addr}

            # create the device
            device = Device(data)
            device.save()
        
        return device

    # ONCE DATABASE IS READY TO ACCEPT CONNECITIONS
    def setup_rpi(self):
        data = {}

        # 1-set the raspbeerypi device information CREATE A DEVICE in db
        # check or create the threshold
        device = self.get_or_create_device()

        # 2-create the threshold
        # check or create the threshold
        threshold = self.get_or_create_threshold()
        data.update(threshold=threshold)

        # 3 - check or create the wifi
        # check or create the wifi
        wifi = self.get_or_create_wifi()
        data.update(wifi=wifi)

        # 4 get or create the first measurement (for testing porpuses)
        measurement = self.get_or_create_measurement()

        # update device with new trheshold, wifi and measurement
        device.measurements.extend([measurement])
        device.update(data)
        
        # Testing
        print(
            device.ip_addr, device.mac_addr, device.netmask, device.threshold, device.wifi,
            device.threshold.soil_ph_min, device.threshold.device_id,
            device.wifi.ssid, device.wifi.password, device.wifi.device_id,
            device.measurements, 
            device.measurements[0].air_temp,
        )

if __name__ == '__main__':
    # 0 db - instanciate obj
    db_setup = DatabaseSetUp()

    # 1 db - setup and installation (init, migrate, upgrade)
    db_setup.init_db()

    # 2 db - add default data (device, threshold, wifi, measurement) 
    db_setup.setup_rpi()