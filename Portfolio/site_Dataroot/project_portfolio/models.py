from django.db import models
from django.contrib.auth.models import UserManager, User

class MyUser(User):
    email_address = models.CharField(max_length=100, verbose_name="Почта") 
    picture = models.FileField(upload_to='media/images/', verbose_name="Загрузка фото", blank=True, null=True)
    company = models.CharField(max_length=150, verbose_name='Компания', blank=True, null=True)

    objects = UserManager()
      
    ''' Imitation model of the user and 
 	the addition of fields. '''

class Projects(models.Model):
	''' Creating a model of the Projects. '''

	name = models.CharField(max_length=200, verbose_name="Названия проекта")
	projectCompany = models.ForeignKey(MyUser)

	def __str__(self):
		return self.name

class Link(models.Model):
	''' Creating a model of the Link. '''

	url = models.TextField(verbose_name="Ссылка")
	urlProject = models.ForeignKey(Projects)

	def __str__(self):
		return self.url

