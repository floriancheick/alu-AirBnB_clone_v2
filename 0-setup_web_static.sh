#!/usr/bin/env bash
# Server file system for deployment

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# Configure file system
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /dtat/web_static/releases/test/ /data/web_static/current


sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '55i location /hbnb_static {\nalias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default


sudo service ngnix restart
