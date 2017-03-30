from django.shortcuts import render
from models import Project, Technology, ProjectImage

# Create your views here.
def project_portfolio(request):
	prj_obj_list = Project.objects.all()
	tech_list = Technology.objects.all()
	for prj in prj_obj_list:
		image = prj.images
		print 'image',image
	data = {'prj_obj_list':prj_obj_list, 'tech_list':tech_list}

	return render(request, 'index.html', data)

