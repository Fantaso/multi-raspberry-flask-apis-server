from datetime import datetime

# DEFAULT DATA - (TO INITLIZIED IMPORTANT DATA ON FIRST BOOT)

# WIFI
wifi_data = {'ssid': 'NETGEAR09', 'password':'dizzycream794'}

# MEASUREMENT
measurement_data = {
    'soil_ph': 5.5475,
    'soil_temp': 18.7542,
    'soil_humi': 88.5420,
    'air_temp': 17.4565,
    'air_humi': 55.5412,
    'air_pres': 22.2525,
    'alarm_status': False,
    'batt_status': 100,
    'timestamp': datetime.now(),
}

# THRESHOLD
threshold_data = {
    'soil_ph_min': 5,
    'soil_ph_max': 8,
    'soil_temp_min': 10,
    'soil_temp_max': 30,
    'soil_humi_min': 15,
    'soil_humi_max': 100,
    'air_temp_min': 5,
    'air_temp_max': 35,
    'air_humi_min': 10,
    'air_humi_max': 80,
    'air_pres_min': 8,
    'air_pres_max': 100,
}