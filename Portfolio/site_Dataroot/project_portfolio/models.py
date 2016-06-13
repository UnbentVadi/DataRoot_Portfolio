from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class MyUser(AbstractUser):
    # email = models.CharField(max_length=100, verbose_name="Почта")
    picture = models.CharField(max_length=100, verbose_name="Фото", blank=True, null=True)
    company = models.CharField(max_length=150, verbose_name='Компания', blank=True, null=True)

    objects = UserManager()


class Projects(models.Model):
    name = models.CharField(max_length=200, verbose_name="Названия проекта")
    project_company = models.ForeignKey(MyUser)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.TextField(verbose_name="Ссылка")
    url_project = models.ForeignKey(Projects)

    def __str__(self):
        return self.url
