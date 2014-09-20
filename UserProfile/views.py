from django.shortcuts     import render
from django.http          import HttpResponse, HttpResponseRedirect
from django.template      import RequestContext
from django.shortcuts     import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

# Create your views here.
from django.views.generic import ListView


#Pinax
from account import urls, models

from deal.forms import CreateDealForm
from UserProfile.models import Profile

def index(request):
    #RequestContext gets the info on user's request
    context = RequestContext(request)

    #defines python variables for HTML files.
    #{{boldmessage}} will display "I am bold font from the context"
    #in the HTML
    context_dict = {'boldmessage': "I am bold font from the context",
            }
    return render_to_response('deal/deal_index.html', context_dict, context)

# Create your views here.
def profile_check_login(request):
    if not request.user.is_authenticated():
        #redirect to login page
        #this is bad practice, but I can't see to resolve it
        return HttpResponseRedirect('/account/login')

    user = request.user
    user_account = models.Account.objects.get(user_id=user.id)


    try:
        profile = Profile.objects.get(account_id=user_account.id)
    except Profile.DoesNotExist:
        profile = Profile.objects.create_profile(user_account)
    return render(request, 'profile_index.html', { 'profile': profile,
                                                   'user':    user
                                                  })

