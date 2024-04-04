#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
Autor : Said LAMGHARI
"""

from fabric.api import run, put, env
import os

# Définit les hôtes et l'utilisateur pour Fabric
env.hosts = ['54.242.107.147', '54.236.27.110']
# Mettez à jour avec votre nom d'utilisateur
env.user = 'ubuntu'
# Mettez à jour avec le chemin de votre clé privée SSH
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Archive to the web servers
    Args:
        archive_path : The archive file to be deployed
    Returns:
        bool: True or False
    """
    if not os.path.exists(archive_path):
        return False

    # Obtient le nom du fichier d'archive
    archvnm = os.path.basename(archive_path)
    # Obtient le nom du dossier de l'archive (en enlevant l'extension)
    archvfd = archvnm.split('.')[0]
    # # Chemin distant pour l'archive
    rmtp = "/data/web_static/releases/{}/".format(archvfd)

    try:
        # Télécharge l'archive sur le serveur distant
        put(archive_path, "/tmp/")
        # Crée le chemin distant
        run("mkdir -p {}".format(rmtp))
        # Extrait l'archive
        run("tar -xzf /tmp/{} -C {}".format(archvnm, rmtp))
        # Supprime le fichier d'archive temporaire
        run("rm /tmp/{}".format(archvnm))
        # Déplace les fichiers vers l'emplacement approprié
        run("mv {}web_static/* {}".format(rmtp, rmtp))
        # Supprime le répertoire web_static redondant
        run("rm -rf {}web_static".format(rmtp))
        # Supprime le lien symbolique "current" actuel
        run("rm -rf /data/web_static/current")
        # Crée un nouveau lien symbolique
        run("ln -s {} /data/web_static/current".format(rmtp))
        return True
    except Exception as e:
        # Affiche l'erreur pour le débogage
        print("Exception occurred:", str(e))
        return False
