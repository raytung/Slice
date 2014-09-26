from django.shortcuts     import render, redirect
from django.http          import HttpResponse, HttpResponseRedirect
from django.template      import RequestContext
from django.shortcuts     import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import ListView


#Pinax
from account import urls, models

from UserProfile.models import Profile
from UserProfile.forms import EditAccountForm

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

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            acc = form.save(commit=False)

            #telling Django that we're only updating these 2 fields in the model
            acc.save(update_fields=["first_name",
                                    "last_name"])
            #need to redirect so we won't get stuck at POST.
            #try removing the following line and test out the save function.
            #after you saved, try refreshing the page.
            return redirect('profile_index')

    profile = Profile.objects.get(account_id=user_account.id)
    return render(request, 'profile_index.html', { 'profile': profile,
                                                   'user':    user,
                                                  })
def edit_profile(request):
    if not request.user.is_authenticated():
        #redirect to login page
        #this is bad practice, but I can't see to resolve it
        return HttpResponseRedirect('/account/login')

    user = request.user
    user_account = models.Account.objects.get(user_id=user.id)
    form = EditAccountForm()

    return render(request, 'profile_edit.html', {'edit_form': form })


