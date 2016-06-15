# DataRoot_Portfolio
​
# Synopsis
​
​
---
# Quickly start
​
Запуск проекта
​
В командній строкі запустити команду
​
```console
cd ~
virtualenv --python=python3.4 env
source /home/vagrant/env/bin/activate
​
sudo apt-get install mysql-server
​
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
*Якщо у вас вже встановлена БД main:
drop DATABASE main;
CREATE DATABASE main;
​
Вийдіть, натиснувши Ctrl+C
sudo apt-get install python3-dev libmysqlclient-dev
pip install mysqlclient
​
cd /vagrant/Portfolio/
pip install -r requirements.txt
​
​
cd /vagrant/Portfolio/site_Dataroot
​
python3 manage.py createsuperuser
Введіть свій логін:
Введіть свій em@il:
Введіть свій пароль:
​
python manage.py makemigrations
python manage.py migrate
cd /vagrant/
sh script.sh
​
В браузері ввести url
​
```console
localhost:8000
​
​
```
---
# Start on server
​
​
[back to top](#synopsis)
