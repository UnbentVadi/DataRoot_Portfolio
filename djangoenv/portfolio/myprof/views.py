from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/profile')
        else:
            args['login_error'] = 'No such user'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def template_three_simple(request):
        return render_to_response('profile.html', {'name': request.user.username})