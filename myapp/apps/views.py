from django.http import HttpResponse
from django.template import loader
from .models import App

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
	template_path = 'apps/upload.html'
	context = {
		'title': 'Upload'
	}
	return print_response(request,template_path,context)

def detail(request, app_id):
	template_path = 'apps/detail.html'
	app = App.objects.get(id=app_id)
	template = loader.get_template('apps/detail.html')
	context = {
		'app': app,
		'id':app_id,
	}
	return print_response(request,template_path,context)

def edit(request, app_id):
	template_path = 'apps/edit.html'
	app = App.objects.get(id=app_id)
	context = {
		'app': app,
		'title': 'Edit'
	}
	return print_response(request,template_path,context)

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
