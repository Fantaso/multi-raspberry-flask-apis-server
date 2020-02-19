from psutil import net_if_addrs
from subprocess import PIPE 
from netaddr import IPNetwork
import subprocess
import ipaddress


class WlanSetUp():
    """SetUp the network configurations at bootup of RaspberryPI."""
    def __init__(self, interface='w', *args, **kwargs):
        self.ssid = None
        self.password = None
        






# ONCE CONNECTED TO WLAN
# 1-scan ip availables
# 2-send request to all available ips
# 3-send mac-ip and request client to register the device

# ONCE REGISTERED WITH CLIENT
# 1-activate raspberrypi API