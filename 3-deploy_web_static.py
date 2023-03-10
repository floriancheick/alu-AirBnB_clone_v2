#!/usr/bin/python3
"""Comment"""
from fabric.api import *
import os
import re
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['52.55.249.213', '54.157.32.137']


def do_pack():
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(datetime.strftime(
        datetime.now(),
        "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(filename))
    if result.failed:
        return None
    return filename


def do_deploy(archive_path):
    """Comment"""
    if not os.path.isfile(archive_path):
        return False

    filename_regex = re.compile(r'[^/]+(?=\.tgz$)')
    match = filename_regex.search(archive_path)

    # Upload the archive to the /tmp/ directory of the web server
    archive = match.group(0)
    result = put(archive_path, "/tmp/{}.tgz".format(archive))
    if result.failed:
        return False

    result = run(
        "mkdir -p /data/web_static/releases/{}/".format(archive))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
                 .format(archive, archive))
    if result.failed:
        return False

    # Delete the archive from the web server
    result = run("rm /tmp/{}.tgz".format(archive))
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/{}"
                 "/web_static/* /data/web_static/releases/{}/"
                 .format(archive, archive))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{}/web_static"
                 .format(archive))
    if result.failed:
        return False

    # Delete the symbolic link /data/web_static/current from the web server
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False

    #  Create a new the symbolic link
    result = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                 .format(archive_filename))
    if result.failed:
        return False

    return True


def deploy():
    """Deploy"""
    archive_pack = do_pack()
    if archive_pack is None:
        return False
    deployed = do_deploy(archive_pack)
    return deployed
