from django.conf.urls import patterns, url
from UserProfile import views
import Pledge.views
from django.views.generic import TemplateView

from Pledge.models import Commitment

#performance!!
#also, will have problem if no deals in database

commitment = Commitment.objects.all()
max_id = 0
if commitment:
        max_id = Commitment.objects.all().order_by("-id")[0].id
length = len(str(max_id))


pledge_detail_regex = r'([0-9]{1,'+ str(length)  +'})/'



urlpatterns = patterns('',
                # <root domain>/deal/ will map to our index
        url(r'^$', views.profile_check_login, name="profile_index"),
        url(r'^edit/description/$', views.edit_description, name="profile_edit_description"),
        url(r'^edit/contact/$', views.edit_contact, name="profile_edit_contact"),
        url(r'^edit/$', views.edit_profile, name="profile_edit"),
        url(r'^mydeals/$', views.my_deals, name="profile_mydeals"),
        url(r'^history/$', views.history, name="profile_history"),
        url(r'^myslice/'+pledge_detail_regex+'edit/$', Pledge.views.pledge_edit, name="pledge_edit"),
        url(r'^myslice/$', views.myslice, name="profile_myslice"),
        url(r'^bookmarks/$', views.bookmarks, name="profile_bookmarks"),
        
)