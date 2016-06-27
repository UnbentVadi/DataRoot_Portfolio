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
	sort_changes = sorted(sort_changes, key=lambda links_list: links_list.publish, reverse=True)
	return sort_changes


class MyUserDetailView(DetailView):
	"""
	Accepts the request for showing profile page 
	and provides the context of the myuser_detail.html file
	"""
	model = MyUser

	def get_context_data(self,**kwargs):
		context = super(MyUserDetailView, self).get_context_data(**kwargs)
		project_company = self.kwargs['pk']
		context['projects'] = Projects.objects.filter(project_company = project_company)
		user = MyUser.objects.get(pk=self.kwargs['pk'])
		user_projects = user.projects_set.all()
		changes = []
		for i in range(len(user_projects)):
			project_links = Link.objects.filter(url_project = user_projects[i])
			changes.append(project_links)
		context['ten_changes']= sort_links(changes)[:10]
		context['three_changes']= sort_links(changes)[:3]
		return context


class LinkListView(ListView):
	"""
	Accepts the request for showing list of urls of some project 
	and provides the context of the links_list.html file
	"""
	model = Link

	def get_context_data(self, **kwargs):
		context = super(LinkListView, self).get_context_data(**kwargs)
		url_project_id = self.kwargs['projectname_id']
		context["links"] = Link.objects.filter(url_project_id = url_project_id)
		return context

