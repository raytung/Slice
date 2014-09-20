from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

# Create your views here.
from deal.models import Deal
from django.views.generic import ListView


#Pinax
from account import urls

from deal.forms import CreateDealForm

def index(request):
    #RequestContext gets the info on user's request
    context = RequestContext(request)

    #defines python variables for HTML files.
    #{{boldmessage}} will display "I am bold font from the context"
    #in the HTML
    context_dict = {'boldmessage': "I am bold font from the context",
            }
    return render_to_response('deal/deal_index.html', context_dict, context)


def check_is_login(request):
    if not request.user.is_authenticated():
        #redirect to login page
        #this is bad practice, but I can't see to resolve it
        return HttpResponseRedirect('/account/login')


# Create your views here.
def create_deal_check_login(request):
    check_is_login(request)

    if request.method == 'POST':
        form = CreateDealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.save()
            form ="<div class=\"alert alert-success\" role=\"alert\"> You have successfuly made a deal!</div>"
        else:
            form = "<div class=\"alert alert-danger\" role=\"alert\"> Something is not right. Please try again later. </div>"
    else:
        form = CreateDealForm()
    return render(request, 'create_deal.html', { 'form': form,
                                                 'requst': request })

