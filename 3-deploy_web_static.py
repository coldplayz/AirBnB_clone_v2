#!/usr/bin/python3
'''
Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
'''
from fabric.api import *
from datetime import datetime

# env.user = 'ubuntu'
# env.hosts = ['54.146.64.105', '54.90.28.253']
# env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    ''' Packs a .tgz archive.
    '''
    local("mkdir -p versions")
    dtString = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filePath = 'versions/web_static_{}.tgz'.format(dtString)
    res = local("tar -czvf {} web_static/".format(filePath))
    if res.succeeded:
        return filePath


env.user = 'ubuntu'
env.hosts = ['54.146.64.105', '54.90.28.253']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    ''' Distributes an archive to my web servers.
    '''
    try:
        local("ls {}".format(archive_path))
    except BaseException:
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        op = put(archive_path, '/tmp/')

        # Parse out file name from argument
        filePathList = archive_path.split('/')
        fileName = filePathList[len(filePathList) - 1]
        fileNameNoExt = fileName.split('.')[0]

        # Create required directory if not exists
        op = run(
                "mkdir -p /data/web_static/releases/{}".format(fileNameNoExt))

        # Unpack archive to required directory
        op = run(
                "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                    fileName, fileNameNoExt))

        # Delete the archive from the server
        op = run("rm -rf /tmp/{}".format(fileName))

        # Move contents of archive to right directory
        op = run(
                "cp -r /data/web_static/releases/{}/web_static/*\
                        /data/web_static/releases/{}/".format(
                    fileNameNoExt, fileNameNoExt))

        # Delete redundant web_static folder
        op = run(
                "rm -rf /data/web_static/releases/{}/web_static".format(
                    fileNameNoExt))

        # Ensure the directories and files
        # have the right permissions to avoid 403
        op = sudo("chmod -R 755 /data/web_static/")

        # Delete the symbolic link `current`
        op = run("rm -rf /data/web_static/current")

        # Create new symbolic link
        op = run(
                "ln -s -T /data/web_static/releases/{}/\
                        /data/web_static/current".format(fileNameNoExt))

        return True
    except BaseException:
        return False


def deploy():
    ''' Creates and distributes an archive to my web servers.
    '''
    # Set a constant archive path for multiple invocations in a session
    deploy.n = getattr(deploy, 'n', 0) + 1
    if deploy.n == 1:
        path = do_pack()
        deploy.path = path

    if not deploy.path:
        return False

    return do_deploy(deploy.path)
