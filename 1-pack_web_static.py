#!/usr/bin/python3
"""
Fabric that generates atgz archive
from the contents of the web_static
Autor : Said LAMGHARI

"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """tgz archive from the contents
    of the web_static folder"""

    # Obtient le temps actuel
    timenow = datetime.now()

    # Construit le nom de l'archive avec un horodatage
    archvnm = "versions/web_static_{}.tgz"
    .format(timenow.strftime("%Y%m%d%H%M%S"))

    # Crée le répertoire 'versions' s'il n'existe pas déjà
    local("mkdir -p versions")

    # Exécute la commande 'tar' pour créer l'archive
    rslt = local("tar -czvf {} web_static".format(archvnm))

    # Vérifie si l'exécution de la commande 'tar' a échoué
    # retourne None en cas d'échec
    if rslt.failed:
        return None
    else:
        return archvnm
