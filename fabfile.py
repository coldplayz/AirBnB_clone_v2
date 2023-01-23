#!/usr/bin/python3
'''
'''
from fabric.api import *
from datetime import datetime


def do_bkup():
    ''' Packs a .tgz archive backup of file system to .bkup folder
    '''
    local("mkdir -p .bkups")
    dtString = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filePath = '.bkups/bkup_{}.tgz'.format(dtString)
    res = local("tar -czvf {} *".format(filePath))
    if res.succeeded:
        return filePath
