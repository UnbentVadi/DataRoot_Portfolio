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
    Progress = '/static/image/in_progress.svg'
    Finish = '/static/image/Finish.svg'
    Start = '/static/image/pages.svg'
    
    name_url = models.CharField(verbose_name="Название ссылки", max_length=50, default=None) 
    url = models.TextField(verbose_name="Ссылка")
    publish = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время") 
    process = models.CharField(max_length=60,choices=((Progress,"В процессе разработке"),(Finish, "Готовая страница"),(Start,'Новая страница')), 
        verbose_name = "Прогресс розработки", default=Start)
    url_project = models.ForeignKey(Projects)

    def __str__(self):
        return self.name_url
