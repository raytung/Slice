from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.template  import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

# Create your views here.
from django.views.generic import ListView


#Pinax
from account import urls

#Self defined
from deal.forms  import CreateDealForm, SearchDealForm
from deal.models import Deal


def index(request):
    context = RequestContext(request)
    deals = Deal.objects.all().select_related('UserProfile_Profile')

    context_dict = {'deals': deals,
                    'search_form': SearchDealForm() }

    #if nothing is entered/ selected, display top 5 deals
    #else, search.


    return render_to_response('deal_index.html', context_dict, context)

def create_deal_check_login(request):
    #redirect if not logged in
    if not request.user.is_authenticated():
       return HttpResponseRedirect('/account/login')

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
        search_form = SearchDealForm()
    return render(request, 'create_deal.html', { 'form': form,
                                                 'request': request,
                                                 'search_form': search_form})

