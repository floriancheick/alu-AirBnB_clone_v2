#!/usr/bin/python3
"""
Compress web static package
"""
from os import path
from datetime import datetime
from fabric.api import *


env.hosts = ['52.55.249.213','54.157.32.137']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive):
	if os.path.exists(archive) is False:
		return False
	try:
		put(archive, "/tmp/")
		file = archive.split("/"[-1]
		file_name = file.split(".")[0]
		folder = "/data/web_static/releases/{}/".format(file_name)
		run("mkdir -p {}".format(folder))
		run("tar -xzf /tmp/{} -C {}".format(file, folder))
		run("rm -r /tmp/{}".format(file))
		run("mv {}web_static/* {}".format(folder, folder))
		run("rm -rf {}web_static".format(folder))
		run("rm -rf /data/web_static/current")
		run("ln -s {} /data/web_static/current".format(folder))
		return True
	except Exception:
		return False
