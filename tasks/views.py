from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from google.appengine.api import users
from tasks.models import Account, Task

def index(request):
	return respond(request, 'tasks/index.html')

def list_tasks(request):
	tasks = Task.all().fetch(10)
	return respond(request, 'tasks/list_tasks.html', { 'tasks': tasks })

def new_task(request):
	task = Task(
		body=request.POST['body'],
		description=request.POST['description'])
	task.put()
	return HttpResponseRedirect(reverse('tasks.views.list_tasks'))

def respond(request, template, params=None):
	if params is None:
		params = {}
	
	if request.user is not None:
		account = Account.current_user_account
	
	params['user'] = request.user
	params['is_admin'] = request.user_is_admin
	
	full_path = request.get_full_path().encode('utf-8')
	if request.user is None:
		params['sign_in'] = users.create_login_url(full_path)
	else:
		params['sign_out'] = users.create_logout_url(full_path)
	
	return render_to_response(template, params)