#!/usr/bin/env bash
# default update
echo "Start Bootstrap.sh"

sudo apt-get update

# locals
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales

# time to UTC
sudo unlink /etc/localtime
sudo ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime

# default setups
sudo apt-get -y install g++ gcc python-software-properties build-essential git curl python-dev libpq-dev libbz2-dev libncurses5-dev libreadline6-dev libsqlite3-dev libgdbm-dev liblzma-dev tk8.6-dev libssl-dev python3-setuptools python3-dev libmysqlclient-dev

# add postgres
# sudo apt-get -y install postgresql postgresql-contrib

# add redis
# sudo add-apt-repository ppa:chris-lea/redis-server

# update
sudo apt-get -y update

# install redis
# sudo apt-get -y install redis-server

# python virtualenv
sudo apt-get -y install python-virtualenv

#install ngix supervisor

# sudo apt-get -y install nginx
# sudo apt-get -y install supervisor

# Make virtual env
cd ~
virtualenv --python=python3.4 env
source /home/vagrant/env/bin/activate
cd ~/vagrant
pip install -r requirements.txt



# # Set Coupon Environment
# sudo cat >> /home/vagrant/.bashrc <<- EOM
# #Coupon Environment
# export COUPON_ENVIRONMENT=local
# EOM

# . /home/vagrant/.bashrc


#l/etc/defult/locals
