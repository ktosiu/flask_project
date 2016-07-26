from os import system as cmd

cmd('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927')
cmd('echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list')
cmd('apt-get update')
cmd('apt-get -y install mongodb-org')
cmd('apt-get -y install upstart-sysv')
