#!/usr/bin/env bash
# Sets up my web servers for rhe deployment of web_static.


sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo ln -sfr -T /data/web_static/releases/test /data/web_static/current

# Create a basic html file to test
body='<!DOCTYPE html>
<html>
	<head>
		<title>Intro Page</title>
	</head>
		<body>
			<h1>Welcome to Greenbel homepage!</h1>
		</body>
</html>'

sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/

echo "$body" > /data/web_static/releases/test/index.html

# See if the desired location block exists
location=$(sudo grep "	location ^~ /hbnb_static {" /etc/nginx/sites-available/default)

if [ -z "$location" ]
then

	# Append a location block for /hbnb_static
	sudo sed -i '/server_name _/a\\n\tlocation ^~ /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

sudo service nginx restart
