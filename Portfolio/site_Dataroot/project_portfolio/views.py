from django.shortcuts import render
from django.shortcuts import render_to_response

def profile1(request):
	view = 'profile1'
	return render_to_response('first_profile.html', {'name': view})