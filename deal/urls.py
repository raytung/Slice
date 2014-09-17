from django.conf.urls import patterns, url
from deal import views

'''
	Just like Slice/urls.py, we have a urlpatterns object. 
	Unlike Slice/urls.py, we are not mapping regex to apps
	we are mapping regex to html page. 

'''
urlpatterns = patterns('', 
		# <root domain>/deal/ will map to our index
        url(r'^$', views.index),
        )
