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
    try:
        local("mkdir -p versions")
        dtString = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        filePath = 'versions/web_static_{}.tgz'.format(dtString)
        res = local("tar -czvf {} web_static/".format(filePath))
        return filePath
    except:
        return None
