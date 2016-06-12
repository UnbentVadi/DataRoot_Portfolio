from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib.auth.hashers import check_password


def login(request):
    if request.user.is_authenticated() is True:
        return redirect('/profile')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '':
            args['login_error'] = 'Enter username'
            return render_to_response('login.html', args)
        if password == '':
            args['login_error'] = 'Enter password'
            return render_to_response('login.html', args)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            args['login_error'] = 'incorrect login'
            return render_to_response('login.html', args)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/profile')
        else:
            args['login_error'] = 'incorrect password'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def template_three_simple(request):
    if request.user.is_authenticated() is True:
        return render_to_response('profile.html', {'name': request.user.username})
    return redirect('/')
