from project_portfolio.models import MyUser, Projects, Link
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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
	Accepts the request for showing profile, updates or settings page 
	and provides the context of their html file
	"""
	model = MyUser

	def get_context_data(self,**kwargs):
		context = super(MyUserDetailView, self).get_context_data(**kwargs)
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
		return context


class LinkDeatailView(MyUserDetailView):
	"""
	Accepts the request for showing project page
	and provides the context of the project.html file
	"""
	model = Link

	def get_context_data(self, **kwargs):
		context = super(LinkDeatailView, self).get_context_data(**kwargs)
		url_project_id = self.kwargs["projectname_id"]
		context["project_name"] = Projects.objects.get(id = url_project_id)
		context["links"] = Link.objects.filter(url_project_id = url_project_id)
		return context
