from project_portfolio.models import MyUser, Projects, Link
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class MyUserDetailView(DetailView):
	# Accepts the request for showing profile page 
	# and provides the context of the myuser_detail.html file
	model = MyUser
	def get_context_data(self,**kwargs):
		context = super(MyUserDetailView, self).get_context_data(**kwargs)
		project_company = self.kwargs['pk']
		context['projects'] = Projects.objects.filter(project_company= project_company)
		return context

class LinkListView(ListView):
	# Accepts the request for showing list of urls of some project 
	# and provides the context of the links_list.html file
	model = Link
	def get_context_data(self, **kwargs):
		context = super(LinkListView, self).get_context_data(**kwargs)
		url_project_id = self.kwargs['projectname_id']
		context["links"] = Link.objects.filter(url_project_id = url_project_id)
		return context

