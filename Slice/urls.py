from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from Slice import views

'''
Maps URL to webpages
	- Uses regex
	partterns(A, url(B, C))

	A = the base url. 
		i.e if you have multiple url and they all start with the same prefix
		e.g instead of 
				patterns("", 
					url(r"^cakeyface/admin", include(whatever)),
					url(r"^cakeyface/powder", include(whatever))
						// ... etc
					)
			we can go
				patterns("^cakeyface",
					url(r"^admin", include(whatever)),
					url(r"^powder", include(whatever))
					)
	
	B = the regex you need to map the url.
		e.g r"^admin/" maps <our domain root>/admin/ to admin.site.urls

	C = include(). The site we maps the defined URL to.
		We map to the app's urls.py file
		The app's urls.py file will the direct us to the actual page we want.
		More on that in Deal/urls.py
'''
urlpatterns = patterns("",
    url(r"^$", views.index, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^profile/", include("UserProfile.urls")),
    url(r"^deals/", include('deal.urls')),
    url(r"^about/$", TemplateView.as_view(template_name="about_us.html"), name="about"),
    url(r"^support/$", TemplateView.as_view(template_name="support.html"), name="support"),
    url(r"^users/", include('Users.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
