#!/usr/bin/python3
"""
Deploy web static 
"""
from os import path
from datetime import datetime
from fabric.api import *

env.hosts = ['52.55.249.213', '54.157.32.137']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
	try:
		local("mkdir -p versions")
		archive = "versions/web_static_{}.tgz".format(strftime("%Y%M%d%H%M%S%"))
		local("tar -cvzf {} web_static/".format(archive))

		return archive
	except Exception:
		return None
