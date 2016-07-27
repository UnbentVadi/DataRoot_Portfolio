from project_portfolio.models import MyUser, Projects, Link
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from project_portfolio.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

def sort_links(links_list):
	"""
	Sort links_list by chenging date
	"""
	sort_changes = []
	for i in range(len(links_list)):
		for j in range(len(links_list[i])):
			sort_changes.append(links_list[i][j])
	sort_changes = sorted(sort_changes, key=lambda x: x.publish, reverse=True)
	return sort_changes 

class MyUserDetailView(DetailView):
	"""
	Accepts the request for showing profile page 
	and provides the context of the myuser_detail.html file
	"""
	model = MyUser

	def get_context_data(self,**kwargs):
		profile_form = ProfileForm
		context = super(MyUserDetailView, self).get_context_data(**kwargs)
		context.update(csrf(self.request))
		project_company = self.kwargs["pk"]
		context["projects"] = Projects.objects.filter(project_company = project_company)
		user = MyUser.objects.get(pk=self.kwargs["pk"])
		context["name"] = user
		user_projects = user.projects_set.all()
		context["projects_count"] = len(user_projects)
		changes = []
		for i in range(len(user_projects)):
			project_links = Link.objects.filter(url_project = user_projects[i])
			changes.append(project_links) 
		context["all_links"] = sort_links(changes)[:15]
		context["four_changes"] = sort_links(changes)[:4]
		context["five_changes"]= sort_links(changes)[:5]
		context["form"] = profile_form(instance=user)
		context['progress'] = Link.objects.filter(process = '/static/image/in_progress.svg')
		context['finish'] = Link.objects.filter(process = '/static/image/Finish.svg')
		context['start'] = Link.objects.filter(process = '/static/image/pages.svg')
		return context


class LinkDeatailView(MyUserDetailView):
	"""
	Accepts the request for showing list of urls of some project 
	and provides the context of the links_list.html file
	"""
	model = Link

	def get_context_data(self, **kwargs):
		context = super(LinkDeatailView, self).get_context_data(**kwargs)
		url_project_id = self.kwargs["projectname_id"]
		context["project_name"] = Projects.objects.get(id = url_project_id)
		context["links"] = Link.objects.filter(url_project_id = url_project_id)
		return context

def iframe_page(request, pk):
	link = get_object_or_404(Link, pk=pk)
	return render(request, "project_portfolio/modal_window.html", {'link':link})

@login_required
def EditProfile(request, pk):
	if request.POST:
		user = request.user
		userform = ProfileForm(request.POST or None, instance = user)
		args = {}
		if userform.is_valid():
			userform.save()
			return redirect('/profile/%s/settings' % pk)
		else:
			args["error"] = "Error enter"
	else:
		userform = ProfileForm()
	return redirect('/profile/%s/settings' % pk)

