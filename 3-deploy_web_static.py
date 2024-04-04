#!/usr/bin/python3
"""
Fabric script for creating
distributing an archive to web servers.

Author: Said LAMGHARI
"""

from datetime import datetime
import os
from fabric.api import env, local, put, run

# Définit les hôtes et l'utilisateur pour Fabric
env.hosts = ['54.242.107.147', '54.236.27.110']
env.user = 'ubuntu'
# Spécifiez le chemin vers votre clé privée SSH
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Creates a compressed archive
    of the web_static directory."""
    # Génère un horodatage pour le nom de l'archive
    tmstp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archn = "versions/web_static_{}.tgz".format(tmstp)

    # Crée le répertoire 'versions' s'il n'existe pas déjà
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Crée l'archive en utilisant tar
    rlt = local("tar -czvf {} web_static".format(archn))
    if rlt.failed:
        return None
    else:
        return archn


def do_deploy(archive_path):
    """Deploys the archive
    to the web servers."""
    if not os.path.exists(archive_path):
        return False

    archn = os.path.basename(archive_path)
    fldn = archn.split('.')[0]
    remote_path = "/data/web_static/releases/{}/".format(fldn)

    # Transfère l'archive sur le serveur distant
    if put(archive_path, "/tmp/{}".format(archn)).failed:
        return False

    # Déploie l'archive sur le serveur
    cmnds = [
        "mkdir -p {}".format(remote_path),
        "tar -xzf /tmp/{} -C {}".format(archn, remote_path),
        "rm /tmp/{}".format(archn),
        "mv {}web_static/* {}".format(remote_path, remote_path),
        "rm -rf {}web_static".format(remote_path),
        "rm -rf /data/web_static/current",
        "ln -s {} /data/web_static/current".format(remote_path)
    ]

    # Exécute les commandes sur chaque serveur
    for cmnd in cmnds:
        if run(cmnd).failed:
            return False

    return True


def deploy():
    """Creates and deploys an
    archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
