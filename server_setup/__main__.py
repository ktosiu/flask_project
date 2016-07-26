from os import system as cmd
import sys

#45.32.187.145

args = {'project_name':None, 'server_name':None, 'server_admin':None, 'server_alias':None}
for arg in args:
    args[arg] = input(' ' + arg)

if args['server_alias'] != '':
    alias = args['server_alias']
    args['server_alias'] = 'ServerAlias {}'.format(alias)

with open(sys.path[0] + '/apache.config', 'r') as f: config_content = f.read().format(**args)
with open(sys.path[0] + '/wsgi') as f: wsgi_content = f.read().format(project_name=args['project_name'])

print(wsgi_content)


cmd('apt-get -y update')
cmd('apt-get -y install python3-pip python-dev apache2 libapache2-mod-wsgi-py3')
cmd('pip3 install gunicorn flask')
cmd('a2enmod wsgi')
cmd('mkdir /var/www/{project_name}'.format(project_name=args['project_name']))
cmd('mkdir /var/www/{project_name}/webroot'.format(project_name=args['project_name']))
cmd('touch /var/www/{project_name}/webroot/__init__.py '.format(project_name=args['project_name']))

config_path = '/etc/apache2/sites-available/{project_name}.conf'.format(project_name=args['project_name'])
with open(config_path, 'w') as f: f.write(config_content)
with open('/var/www/{project_name}/{project_name}.wsgi'.format(project_name=args['project_name']), 'w') as f: f.write(wsgi_content)


cmd('sudo a2ensite {}'.format(args['project_name']))
cmd('sudo service apache2 restart')





