from project_portfolio.models import MyUser, Projects, Link
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from project_portfolio.forms import ProfileForm, ProfilePictureForm, ProjectsIdForm
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def sort_links_updates(id):
	user_id = MyUser.objects.get(id = id)
	user_projects = user_id.projects_set.all()
	changes = []
	for i in range(len(user_projects)):
		project_links = Link.objects.filter(url_project = user_projects[i])
		changes.append(project_links) 
	links_list = sort_links(changes)
	return links_list


class MyUserDetailView(DetailView):
	"""
	Accepts the request for showing profile page 
	and provides the context of the myuser_detail.html file
	"""
	model = MyUser

	def get_context_data(self,**kwargs):
		profile_form = ProfileForm
		profile_picture = ProfilePictureForm
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
		all_links = sort_links(changes)
		context['links_finish'] = [x for x in all_links if x.process == '/static/image/Finish.svg']
		context['links_progress'] = [x for x in all_links if x.process == '/static/image/in_progress.svg']
		context['links_new'] = [x for x in all_links if x.process == '/static/image/pages.svg']
		status_project = [x for x in all_links if x.process == '/static/image/pages.svg' or x.process == '/static/image/in_progress.svg']
		context['status_project'] = len(status_project)
		context["four_changes"] = sort_links(changes)[:4]
		context["five_changes"]= sort_links(changes)[:5]
		context["form"] = profile_form(instance=user)
		context['picture_form'] = profile_picture(instance=user)
		context["all_links"] = all_links
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
		r = Link.objects.filter(url_project_id = url_project_id)
		context['finish'] = r.filter(process = '/static/image/Finish.svg')
		context['start'] = r.filter(process = '/static/image/pages.svg')
		context['progress'] = r.filter(process = '/static/image/in_progress.svg')
		context['links'] = r
		return context

@login_required
def iframe_page(request, pk ,id):
	link = get_object_or_404(Link, pk = pk) 
	links_list = sort_links_updates(id)
	return render(request, "project_portfolio/modal_window.html", {'link':link, 'links':links_list})

class EditView(MyUserDetailView, UpdateView):
	Model = MyUser
	form_class = ProfileForm

	def form_invalid(self, form, **kwargs):
		return self.render_to_response(self.get_context_data(form=form))		

class EditPictureView(MyUserDetailView, UpdateView):
	Model = MyUser
	fields = ['picture']

def delete_project(request, pk, projectname_id):
	delete_to_project = Projects.objects.get(id=projectname_id)
	delete_to_link = Link.objects.filter(url_project_id=projectname_id)
	print(delete_to_link)
	print(delete_to_project)
	if request.method == 'POST':
		form = ProjectsIdForm(request.POST, instance=delete_to_project)
		if form.is_valid():
			delete_to_link.delete()
			delete_to_project.delete()
			print(delete_to_link)
			print(delete_to_project)
			return redirect('/')



class LinksPaginationView(MyUserDetailView):

	def get_context_data(self, **kwargs):
		context = super(LinksPaginationView, self).get_context_data(**kwargs)
		id = self.kwargs['pk']
		all_links = sort_links_updates(id)
		paginator = Paginator(all_links, 15)
		page = self.request.GET.get('page')
		try:
			context['all_links'] = paginator.page(page)
		except PageNotAnInteger:
			context['all_links'] = paginator.page(1)
		except EmptyPage:
			context['all_links'] = paginator.page(paginator.num_pages)
		return context

