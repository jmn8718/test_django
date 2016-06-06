from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from .models import App, AppForm

def manage_form(request, app, context):
	if request.method == "POST":
		app.file=request.POST.get('file')
		app.description=request.POST.get('description')
		app.link=request.POST.get('link')
		app.access_right=request.POST.get('access_right')
		app.save()
		return HttpResponseRedirect('/apps/'+str(app.id))
	else:
		template_path = 'apps/upload.html'
		return print_response(request,template_path,context)

def print_response(request, template_path, context):
	template = loader.get_template(template_path)
	return HttpResponse(template.render(context, request))

def index(request):
	apps = App.objects.all()
	context = {
		'apps': apps,
		'title': 'Apps'
	}
	template_path = 'apps/index.html'
	return print_response(request,template_path,context)

def upload(request):
	app = App.objects.create(file='',
				  description='',
				  link='',
				  access_right='PU')
	context = {
		'app': app,
		'title': 'Upload',
		'action':'/apps/upload',
		'buttonText':'UPLOAD'
	}
	return manage_form(request, app, context)

def detail(request, app_id):
	template_path = 'apps/detail.html'
	app = App.objects.get(id=app_id)
	context = {
		'app': app,
		'id':app_id,
	}
	return print_response(request,template_path,context)

def edit(request, app_id):
	app = App.objects.get(id=app_id)
	context = {
		'app': app,
		'title': 'Edit',
		'action':'/apps/edit/{{app.id}}'+str(app.id),
		'buttonText':'EDIT'
	}
	return manage_form(request, app, context)

def public(request):
	template_path = 'apps/index.html'
	public_apps = App.objects.filter(access_right='PU')
	context = {
		'apps': public_apps,
		'title': 'Public apps'
	}
	return print_response(request,template_path,context)

def private(request):	
	template_path = 'apps/index.html'
	private_apps = App.objects.filter(access_right='PR')
	context = {
		'apps': private_apps,
		'title': 'Private apps'
	}
	return print_response(request,template_path,context)
