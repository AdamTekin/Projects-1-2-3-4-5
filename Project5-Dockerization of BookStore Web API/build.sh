#! /bin/bash

yum update -y
amazon-linux-extras install docker -y
systemctl start docker
systemctl enable docker
user -a -G docker ec2-user
newgrp docker
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose