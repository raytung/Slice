from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


# Create your views here.
from deal.models import Deal
from django.views.generic import ListView


def index(request):
    #RequestContext gets the info on user's request
    context = RequestContext(request)
    #boldmessage is same as {{ boldmessage }} in our index.html template
    context_dict = {'boldmessage': "I am bold font from the context",
                    }
    return render_to_response('deal/deallist.html', context_dict, context)
    
# Create your views here.
def about(request):
    return HttpResponse("<a href='/deal/'> Home </a>")

