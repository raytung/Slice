from django.conf.urls import patterns, url
from django.contrib.auth.views import login
from deal import views
from django.views.generic import TemplateView


'''
	Just like Slice/urls.py, we have a urlpatterns object. 
	Unlike Slice/urls.py, we are not mapping regex to apps
	we are mapping regex to html page. 

'''
urlpatterns = patterns('', 
		# <root domain>/deal/ will map to our index
        url(r'^$', TemplateView.as_view(template_name="deal_index.html")),
        url(r'^create', views.create_deal_check_login),
        )
