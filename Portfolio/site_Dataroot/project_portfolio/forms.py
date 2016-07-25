
from django.forms import ModelForm
from project_portfolio.models import MyUser

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