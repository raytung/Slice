from django.conf.urls import patterns, url
from deal import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from Pledge.models import Commitment

#performance!!
#also, will have problem if no deals in database
max_id = Commitment.objects.all().order_by("-id")[0].id
length = len(str(max_id))

pledge_detail_regex = r'^([0-9]{1,'+ str(length)  +'})/$'


'''
	Just like Slice/urls.py, we have a urlpatterns object.
	Unlike Slice/urls.py, we are not mapping regex to apps
	we are mapping regex to html page.

'''
urlpatterns = patterns('',
		# <root domain>/deal/ will map to our index
        ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
