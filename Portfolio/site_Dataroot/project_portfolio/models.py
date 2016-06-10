from django.db import models

class accauntUser(models.Model):
    username = models.ForeignKey('auth.User')
    email_address = models.CharField(max_length=100) 
    picture = models.FileField(upload_to='media/images/', blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    

class projectName(models.Model):
	project = models.CharField(max_length=200)
	projectCompany = models.ForeignKey(accauntUser)

	def __str__(self):
		return self.project

class linkAddress(models.Model):
	urlName = models.TextField()
	urlProject = models.ForeignKey(projectName)

	def __str__(self):
		return self.urlName

