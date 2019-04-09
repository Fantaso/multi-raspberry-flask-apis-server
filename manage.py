from src import create_app, db

import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from boot_setup.network_setup import NetworkSetUp

# network data
net = NetworkSetUp()
ip_addr, netmask, mac_addr = net.get_network_info()


app_env = 'development'
app = create_app(app_env)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)
# TODO/ add the configuration of environment to set host and port auto.
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))


if __name__ == '__main__':
  manager.run()