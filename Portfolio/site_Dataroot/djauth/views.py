from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from project_portfolio.models import MyUser



def index(request):
    """
    Function for index page. Redirect to login page.
    """
    return redirect('/login')


def login(request):
    """
    Function for login page. If user is not authenticated,
    function redirect to login page else, open profile page.
    """
    if request.user.is_authenticated() is True:
        return redirect('myprofile/')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '':
            args['login_error'] = 'Enter username'
            return render_to_response('login.html', args)
        if password == '':
            args['login_error_2'] = 'Enter password'
            return render_to_response('login.html', args)
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            args['login_error'] = 'incorrect login'
            return render_to_response('login.html', args)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/myprofile/')
        else:
            args['login_error_2'] = 'incorrect password'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    """
    Function for logout user.
    After logout, function redirect user to login page.
    """
    auth.logout(request)
    return redirect('/')


def myprofile(request):
    """
    Function for profile page.
    If user is authenticated,
    function open profile page.
    """
    if request.user.is_authenticated() is True:
        return redirect('/profile/%s' % request.user.pk)
    return redirect('/')
