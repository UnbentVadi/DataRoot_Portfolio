# DataRoot portfolio
# Quickly start
Consle
​
```console
git clone https://github.com/UnbentVadi/DataRoot_Portfolio.git

cd DataRoot_Portfolio

vagrant up

vagrant ssh

cd ~
virtualenv --python=python3.4 env
source env/bin/activate
​
sudo apt-get install mysql-server
​```
user: root
pasw: root
​```console
mysql -u root -p
# passw: root
​
CREATE DATABASE main
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
​
# exit Ctrl+C
​
cd /vagrant/Portfolio/
pip install -r requirements.txt
​
​
cd /vagrant/Portfolio/site_Dataroot

​python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
login:
em@il:
passw:
​
cd 
ln -s /vagrant/start
sh start

# url

localhost:8000
```
---

# Start on server

[back to top](#quickly-start)
