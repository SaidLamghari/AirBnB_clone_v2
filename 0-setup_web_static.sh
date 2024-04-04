#!/usr/bin/env bash
# Bash script that sets up your web servers
# the deployment of web_static.
# Autor : Said LAMGHARI

# Installe Nginx s'il nest pas déjà Installe
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Crée les répertoires nécessaires s'ils n'existent pas
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Créer un fichier HTML "fake HTML file" (avec un contenu simple, pour tester votre configuration Nginx)
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Crée le lien symbolique
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Donne la propriété à l'utilisateur et au groupe ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Met à jour la configuration de Nginx
NGINX_CONFIG="/etc/nginx/sites-enabled/default"
NGINX_BLOCK="location /hbnb_static { alias /data/web_static/current/; }"
if ! grep -qF "$NGINX_BLOCK" "$NGINX_CONFIG"; then
    sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
fi

# Redémarre Nginx
sudo service nginx restart
