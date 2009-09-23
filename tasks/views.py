from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task

def index(request):
	return render_to_response('tasks/index.html')

def list_tasks(request):
	tasks = Task.all().fetch(10)
	return render_to_response('tasks/list_tasks.html', { 'tasks': tasks })

def new_task(request):
	return HttpResponseRedirect(reverse('tasks.views.list_tasks'))
