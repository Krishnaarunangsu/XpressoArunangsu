import subprocess
import os
from fabric.api import *
from os import path

env.roledefs = {
    'web': ['172.16.12.1', '172.16.12.2', '172.16.12.3',],
    'media': ['172.16.12.4',],
    'staging': ['172.16.12.5',],
    'testing': ['192.168.56.3',],
    'database': ['172.16.12.7', '172.16.12.8',],
}
env.site_list = []
env.root_path = '/var/websites'

### Setup environments
def testing(site=None):
    env.hosts = env.roledefs['testing']
    env.user = 'coordt'
    if site:
        get_site_list(site)


def staging(site=None):
    env.hosts = env.roledefs['staging']
    env.user = 'staginguser'
    if site:
        get_site_list(site)


def production(site=None):
    env.hosts = env.roledefs['web']
    env.user = 'produser'
    if site:
        get_site_list(site)


def get_site_list(site=None):
    if not site:
        site = prompt('Please specify which site (a comma delimited list is accepted): ', validate=r'^[\w-.,]+$')
    if isinstance(site, (tuple, list)):
        env.site_list = site
    else:
        env.site_list = site.split(',')


### Host Tasks
def check_host():
    """
    Check that the host has all the required commands installed
    """
    local("echo Checking for required commands")
    required_commands = ['wget', 'python', 'tar', 'gzip', 'hg', 'sudo', 'chown',
    'chmod', 'patch', 'grep',]
    for command in required_commands:
        run('which %s' % command)


def install_package(package):
    """
    Install a package on a host using apt-get
    """
    sudo('apt-get install %s' % package)


### Site Tasks
def clean(site=None):
    """
    Remove .pyc files from a site. Needs a site parameter specified.
    """
    if not env.site_list:
        get_site_list(site)
    for item in env.site_list:
        full_path = path.join(env.root_path, item)
        sudo("find %s -name '*.pyc' -depth -exec rm {} \;" % full_path)


def info(site=None):
    """
    Get the current revision of a site
    """
    if not env.site_list:
        get_site_list(site)
    for item in env.site_list:
        full_path = path.join(env.root_path, item)
        run('svn info %s | grep Revision' % full_path)


def ls(site=None, flags=''):
    """
    Get a listing of a site
    """
    if not env.site_list:
        get_site_list(site)
    for item in env.site_list:
        full_path = path.join(env.root_path, item)
        run('ls %s %s' % (flags, full_path))


def push(rev=None, externals=False, rel_path='', site=None):
    """
    Push out changes to all the servers.
    """
    if not env.site_list:
        get_site_list(site)
    if not externals:
        ignore=" --ignore-externals"
    else:
        ignore=""
    for item in env.site_list:
        full_path = os.path.join(env.root_path, item, rel_path)
        run('svn info %s | grep Revision' % full_path)
        if rev is None:
            sudo('svn up%s %s' % (ignore, full_path))
        else:
            sudo('svn up%s -r %s %s' % (ignore, rev, full_path))


def ensite(site=None):
        """                                            "
        Enable an Apache site configuration.
        """
        if not env.site_list:
            get_site_list(site)
        for item in env.site_list:
            sudo('a2ensite %s' % item)


def dissite(site=None):
    """
    Disable an Apache site configuration.
    """
    if not env.site_list:
        get_site_list(site)
    for item in env.site_list:
        sudo('a2dissite %s' % item)


### Apache tasks
def restart():
    """
    Restart Apache
    """
    sudo('/etc/init.d/apache2 restart')


def reload():
    """
    Reload Apache settings
    """
    sudo('/etc/init.d/apache2 reload')


def enmod(mod=None):
    """
    Enable an Apache module
    """
    if not mod:
        mod = prompt('Please specify which module to enable (a comma delimited list is accepted): ', validate=r'^[\w-.,]+$')
    mod_list = mod.split(',')
    for item in mod_list:
        sudo('a2enmod %s' % item)


def dismod(mod=None):
    """
    Disable an Apache module
    """
    if not mod:
        mod = prompt('Please specify which module to disable (a comma delimited list is accepted): ', validate=r'^[\w-.,]+$')
    mod_list = mod.split(',')
    for item in mod_list:
        sudo('a2dismod %s' % item)
