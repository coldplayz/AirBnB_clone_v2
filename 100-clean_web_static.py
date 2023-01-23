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
    if local("ls {}".format(archive_path)).failed:
        return False

    # Upload the archive to the /tmp/ directory of the web server
    op = put(archive_path, '/tmp/')
    if op.failed:
        return False

    # Parse out file name from argument
    filePathList = archive_path.split('/')
    fileName = filePathList[len(filePathList) - 1]
    fileNameNoExt = fileName.split('.')[0]

    # Create required directory if not exists
    op = run("mkdir -p /data/web_static/releases/{}".format(fileNameNoExt))
    if op.failed:
        return False

    # Unpack archive to required directory
    op = run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                fileName, fileNameNoExt))
    if op.failed:
        return False

    # Delete the archive from the server
    op = run("rm -rf /tmp/{}".format(fileName))
    if op.failed:
        return False

    # Move contents of archive to right directory
    op = run(
            "cp -r /data/web_static/releases/{}/web_static/*\
                    /data/web_static/releases/{}/".format(
                fileNameNoExt, fileNameNoExt))
    if op.failed:
        return False

    # Delete redundant web_static folder
    op = run(
            "rm -rf /data/web_static/releases/{}/web_static".format(
                fileNameNoExt))
    if op.failed:
        return False

    # Ensure the directories and files have the right permissions to avoid 403
    op = sudo("chmod -R 755 /data/web_static/")
    if op.failed:
        return False

    # Delete the symbolic link `current`
    op = run("rm -rf /data/web_static/current")
    if op.failed:
        return False

    # Create new symbolic link
    op = run(
            "ln -s -T /data/web_static/releases/{}/\
                    /data/web_static/current".format(fileNameNoExt))
    if op.failed:
        return False

    return True


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


def do_clean(number=0):
    ''' Delete old archives locally and remotely.

        Args:
            number (int): the number of newest archives to keep.
            Defaults to zero which also means one archive to keep - the latest
    '''
    try:
        number = int(number)
    except Exception:
        return

    # List files in reverse order of modification time, i.e. from earliest
    res = local("ls -rt versions", capture=True)
    resRemote = run("ls -rt /data/web_static/releases/")

    # Split based on newlines in captured output
    res = res.split('\n')
    resRemote = resRemote.split('\r\n')
    # print(res, resRemote)
    numFiles = len(res)  # number of files in directory
    numRemoteFiles = len(resRemote)
    # print('local===>', numFiles, 'remote===>', numRemoteFiles)

    if number < numFiles:
        # At least one file to be deleted locally
        if number == 0:
            number = 1

        # Get list of files to be deleted
        toDelete = res[:numFiles - number]

        for f in toDelete:
            # Delete the files locally
            local("rm -rf versions/{}".format(f))

    if number < numRemoteFiles:
        # At least one file to be deleted remotely
        if number == 0:
            number = 1

        toDelete = resRemote[:numRemoteFiles - number]

        for f in toDelete:
            run("rm -rf /data/web_static/releases/{}/".format(f))
