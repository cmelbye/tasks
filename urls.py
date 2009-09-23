from django.conf.urls.defaults import *

urlpatterns = patterns('tasks.views',
	(r'^$', 'index'),
	(r'^tasks/$', 'list_tasks'),
	(r'^tasks/new/$', 'new_task'),
)
