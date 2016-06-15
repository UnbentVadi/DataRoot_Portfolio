from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):
    """
    Imitation model of the AbstractUser
    and adding it to the fields. 
    """
    picture = models.CharField(max_length=100, verbose_name="Фото", blank=True, null=True)
    company = models.CharField(max_length=150, verbose_name='Компания', blank=True, null=True)

    objects = UserManager()


class Projects(models.Model):
    """
    Created models projects.
    """
    name = models.CharField(max_length=200, verbose_name="Названия проекта")
    project_company = models.ForeignKey(MyUser)

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    Created models url list.
    """
    url = models.TextField(verbose_name="Ссылка")
    publish = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время") 
    url_project = models.ForeignKey(Projects)

    def __str__(self):
        return self.url

