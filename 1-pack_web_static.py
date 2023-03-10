#!/usr/bin/python3
"""
Compress web static package
"""
from fabric.api import local
from datetime import datetime

def do_pack():
	# Get
	try: 
		local("mkdir -p versions")
		archive = "versions/web_static_{}.tgz".format(strftime("%Y%M%d%H%M%S"))
		local("tar -cvzf {} web_static/".format(archive))

		return archive
	except Exception:
		return None
