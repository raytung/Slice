from django.conf.urls import patterns, url
from UserProfile import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
		# <root domain>/deal/ will map to our index
        url(r'^$', views.profile_check_login, name="profile_index"),
)
