from django import forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from project_portfolio.models import MyUser, Projects

class ProfileForm(ModelForm):
	class Meta:
		model = MyUser
		fields = ['username', 'email']
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			"disabled": "true",
			})
		self.fields['email'].widget.attrs.update({
			"disabled": "true",
			})


class ProfilePictureForm(ModelForm):
	class Meta:
		model = MyUser
		fields = ['picture']

class ProjectsIdForm(ModelForm):
	class Meta:
		model = Projects
		fields = ['id']