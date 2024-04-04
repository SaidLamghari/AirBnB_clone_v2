#!/usr/bin/python3
"""
Fabric (based on the file 2-do_deplo0y_web_static.py)
that creates and distributes
an archive to your web servers

Autor : Said LAMGHARI
"""
from fabric.api import env, local, put, run
import os
from datetime import datetime

# Définit les hôtes et l'utilisateur pour Fabric
env.hosts = ['54.242.107.147', '54.236.27.110']
# Mettez à jour avec votre nom d'utilisateur
env.user = 'ubuntu'
# Mettez à jour avec le chemin de votre clé privée SSH
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Creates a compressed archive
    ofthe web_static"""
    # Génère un horodatage pour le nom de l'archive
    # Obtient le temps actuel
    timstmp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Construit le nom de l'archive avec un horodatage
    archvn = "versions/web_static_{}.tgz".format(timstmp)

    # Crée le répertoire 'versions' s'il n'existe pas déjà
    local("mkdir -p versions")

    # Crée l'archive en utilisant tar
    rslt = local("tar -czvf {} web_static".format(archvn))

    # Vérifie si la création de l'archive a réussi
    if rslt.failed:
        return None
    else:
        return archvn


def do_deploy(archive_path):
    """Archive to the web servers"""
    # Vérifie si le chemin de l'archive existe
    if not os.path.exists(archive_path):
        return False

    # Obtient le nom de l'archive et le nom du dossier
    archvnm = os.path.basename(archive_path)
    # Obtient le nom du dossier de l'archive (en enlevant l'extension)
    archvfd = archvnm.split('.')[0]
    # Chemin distant pour l'archive
    rmtp = "/data/web_static/releases/{}/".format(archvfd)

    try:
        # Télécharge l'archive sur e serveur distant
        put(archive_path, "/tmp/")
        # Crée le répertoire  déploiement sur le serveur
        run("mkdir -p {}".format(rmtp))
        # Extrait l'archive dans le répertoire de déploiement
        run("tar -xzf /tmp/{} -C {}".format(archvnm, rmtp))
        # Supprime l'archive temporaire ur le serveur
        run("rm /tmp/{}".format(archvnm))
        # Déplace les fichiers de l'archive vers répertoire de déploiement
        run("mv {}web_static/* {}".format(rmtp, rmtp))
        # Supprime répertoire 'web_static' redondant
        run("rm -rf {}web_static".format(rmtp))
        # Supprime  lien symbolique 'current' existant
        run("rm -rf /data/web_static/current")
        # Crée  nouveau lien symbolique vers  répertoire de déploiement
        run("ln -s {} /data/web_static/current".format(rmtp))
        return True
    except Exception as e:
        # Affiche l'erreur pour  débogage
        print("Exception occurred:", str(e))
        return False


def deploy():
    """Creates an archive to the web servers
    distributes an archive to the web servers"""
    # Crée l'archive
    achp = do_pack()
    # Vérifie si la création darchive a réussi
    if achp is None:
        return False
    # Déploie l'archive sur serveurs
    return do_deploy(achp)
