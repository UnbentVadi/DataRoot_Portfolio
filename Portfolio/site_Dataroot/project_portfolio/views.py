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
	return sort_changes # [<Link: one more link>, <Link: another link>, <Link: somth>, <Link: new link>, <Link: Link2>, <Link: Link1>]


class MyUserDetailView(DetailView):
	"""
	Accepts the request for showing profile page 
	and provides the context of the myuser_detail.html file
	"""
	model = MyUser

	def get_context_data(self,**kwargs):
		context = super(MyUserDetailView, self).get_context_data(**kwargs)
		project_company = self.kwargs["pk"]
		context["projects"] = Projects.objects.filter(project_company = project_company)
		user = MyUser.objects.get(pk=self.kwargs["pk"])
		context["name"] = user
		user_projects = user.projects_set.all()
		context["projects_count"] = len(user_projects)# [<Projects: Project1>, <Projects: Project2>, <Projects: Project(first_user)>]
		changes = []
		for i in range(len(user_projects)):
			project_links = Link.objects.filter(url_project = user_projects[i])
			changes.append(project_links) # [[<Link: Link1>, <Link: another link>, <Link: one more link>], [<Link: Link2>, <Link: somth>], [<Link: new link>]]
		all_links = Link.objects.all()[:15]
		context["all_links"] = sorted(all_links, key=lambda x: x.publish, reverse=True)
		context["five_changes"]= sort_links(changes)[:5] # {'changes': [<Link: one more link>, <Link: another link>, <Link: somth>, <Link: new link>, <Link: Link2>, <Link: Link1>]}
		context["four_changes"]= sort_links(changes)[:4]
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
