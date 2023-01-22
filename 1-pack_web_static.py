#!/usr/bin/python3
'''
Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
'''
from fabric.api import *
from datetime import datetime

def do_pack():
    ''' Packs a .tgz archive.
    '''
    local("mkdir -p versions")
    dtString = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filePath = f'versions/web_static_{dtString}.tgz'
    res = local(f"tar -czvf {filePath} web_static/")
    if res.succeeded:
        return filePath
