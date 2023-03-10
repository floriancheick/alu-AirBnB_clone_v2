#!/usr/bin/env bash
# Description
sudo apt-get update
sudo apt-get -y install nginx

folders=("/data/web_static/releases/test" "/data/web_static/shared/")

for directory in "${folders[@]}"; do
  #  if [ ! -e "$directory" ]; then
  mkdir -p "$directory"
  #  fi
done

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >/data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
ln --symbolic --force /data/web_static/releases/test /data/web_static/current

# The -R option ensures that the ownership changes are applied
chown -R ubuntu:ubuntu /data/

sed -i '/listen 80 default_server;/a \ \n    location /hbnb_static {\n        alias /data/web_static/current/;\n        index index.html;\n    }' /etc/nginx/sites-available/default

service nginx restart
