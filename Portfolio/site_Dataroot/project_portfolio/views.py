from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from project_portfolio.models import MyUser, Projects, Link

def profile1(request, accauntuser_id):
    return render_to_response('first_profile.html',
        {
        'accauntUser': MyUser.objects.filter(username=accauntuser_id),
        'projects' : Projects.objects.filter(projectCompany=accauntuser_id),
        }
        )
def project_detail(request, projectname_id, accauntuser_id):
    return render_to_response('urls_list.html', 
        {'urls': Link.objects.filter(urlProject_id=projectname_id)})    
        
