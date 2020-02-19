from psutil import net_if_addrs
from subprocess import PIPE 
from netaddr import IPNetwork
import subprocess
import ipaddress
import requests


class NetworkSetUp():
    """SetUp the network configurations at bootup of RaspberryPI."""
    def __init__(self, interface='w', *args, **kwargs):
        self.interface = interface
        self.network_ips_icmp = []
        self.network_ips_http = []
        if self.interface == 'w':
            self.interface = self.get_current_nic_name()
        # if len(self.network_ips_icmp) <= 0:
        #     self.network_ips_icmp = self.scan_network_icmp()
        # if len(self.network_ips_http) <= 0:
        #     self.network_ips_http = self.scan_network_http()
        

    def get_current_nic_name(self):
        # get a list of all network interfaces' names (eth,wlan) of the system 
        nics_names = NetworkSetUp.get_nics_names()
        # gets and return the one matching our interface
        for nic in nics_names:
            if nic.startswith(self.interface):
                return nic

    def get_network_info(self):
        nics = net_if_addrs()
        nic_name = self.get_current_nic_name()
        nic = nics[nic_name]

            # AF_INET: 2 -> for IPv4
            # AF_INET6: 10 -> for IPv6
            # AF_PACKET: 17 -> for NIC mac address
        # get ip address and network mask from interface
        data = [(inet.address, inet.netmask) for inet in nic if inet.family == 2]
        ip_addr, netmask = data[0][0], data[0][1]

        # get mac address
        mac_addr = [inet.address for inet in nic if inet.family == 17][0]

        return ip_addr, netmask, mac_addr


    def scan_network_icmp(self):
        # get nic information
        ip_addr, netmask, mac_addr = self.get_network_info()

        # gets the network address with mask as string from IP address
            # 192.168.1.15/255.255.255.0 -> 192.168.1.0/24
        network_range = str(IPNetwork(ip_addr + '/' + netmask).cidr)
        
        # set the network addr and mask to a 
        network = ipaddress.ip_network(network_range)

        # start the network scan
        network_ips = []
        for addr in network.hosts():
            res = subprocess.call(['ping', '-c', '3', str(addr)], stdout=PIPE) 
            if res == 0:
                print(f'Added: {addr}')
                network_ips.append(addr)
        
        return network_ips

    def scan_network_http(self):
        # get nic information
        ip_addr, netmask, mac_addr = self.get_network_info()

        # gets the network address with mask as string from IP address
            # 192.168.1.15/255.255.255.0 -> 192.168.1.0/24
        network_range = str(IPNetwork(ip_addr + '/' + netmask).cidr)
        
        # set the network addr and mask to a 
        network = ipaddress.ip_network(network_range)
        
        # start the network scan
        network_ips = []
        for addr in network.hosts():
            try:
                print(f'Trying: {addr}')
                url = f'http://{addr}:5000/device'
                req = requests.get(url)
                if req.status_code == requests.status_codes.codes.OK:
                    print(f'Added: {addr}')
                    network_ips.append(addr)
            except requests.exceptions.ConnectionError:
                print(f'The IP address {addr} is not available!')
                pass


    @staticmethod
    def get_nics_names():
        # returns all nics/network interfaces names in a list
        return list(net_if_addrs().keys())





# ONCE CONNECTED TO WLAN
# 1-scan ip availables
# 2-send request to all available ips
# 3-send mac-ip and request client to register the device

# ONCE REGISTERED WITH CLIENT
# 1-activate raspberrypi API