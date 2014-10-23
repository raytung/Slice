from django.conf.urls import patterns, url
from Users import views
from django.views.generic import TemplateView

from UserProfile.models import Profile

profiles = Profile.objects.all()

max_id = 0
if profiles:
    max_id = profiles.order_by("-account_id")[0].account_id
length = len(str(max_id))


user_detail_regex = r'^([0-9]{1,'+ str(length)  +'})/$'

urlpatterns = patterns('',
		# <root domain>/deal/ will map to our index
        url(user_detail_regex, views.users_detail, name="users_detail")
)

