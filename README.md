# DataRoot_Portfolio
# Synopsis
# Quickly start
Consle
​
```console
git clone https://github.com/UnbentVadi/DataRoot_Portfolio.git

cd ~
virtualenv --python=python3.4 env
source /home/vagrant/env/bin/activate
​
sudo apt-get install mysql-server
​
user: root
pasw: root
​
mysql -u root -p
pasw: root
​
CREATE DATABASE main
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
​
# exit Ctrl+C

pip install mysqlclient
​
cd /vagrant/Portfolio/
pip install -r requirements.txt
​
​
cd /vagrant/Portfolio/site_Dataroot
​
python3 manage.py createsuperuser
python3 manage.py createsuperuser
login:
em@il:
passw:
​
python manage.py makemigrations
python manage.py migrate

cd /vagrant/
sh script.sh

# url

localhost:8000
```
---

# Start on server

[back to top](#synopsis)
