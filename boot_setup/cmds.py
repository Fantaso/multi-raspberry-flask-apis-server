import subprocess as sp

def cmds():
    db_init = ['python3','manage.py', 'db', 'init']
    db_migrate = ['python3','manage.py', 'db', 'migrate']
    db_upgrade = ['python3','manage.py', 'db', 'upgrade']
    setup_py = ['python3','setup.py']

    sp.Popen(args=db_init)
    sp.Popen(args=db_migrate)
    sp.Popen(args=db_upgrade)
    sp.Popen(args=setup_py)

if __name__ =='__main__':
    cmds()
    exit()
