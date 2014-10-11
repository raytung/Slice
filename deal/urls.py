from django.conf.urls import patterns, url
from deal import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from deal.models import Deal

#performance!!
#also, will have problem if no deals in database
max_id = Deal.objects.all().order_by("-id")[0].id
length = len(str(max_id))

deal_detail_regex = r'^([0-9]{1,'+ str(length)  +'})/$'


'''
	Just like Slice/urls.py, we have a urlpatterns object.
	Unlike Slice/urls.py, we are not mapping regex to apps
	we are mapping regex to html page.

'''
urlpatterns = patterns('',
		# <root domain>/deal/ will map to our index
        url(r'^$', views.index, name="deals_index"),
        url(r'^create', views.create_deal_check_login, name="deal_create"),
        url(deal_detail_regex, views.detail, name="deal_detail")
        ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
