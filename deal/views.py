from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.template  import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

#https://docs.djangoproject.com/en/1.7/topics/db/queries/#complex-lookups-with-q-objects
from django.db.models import Q

#Pinax
from account import urls

#Self defined
from deal.forms  import CreateDealForm, SearchDealForm
from deal.models import Deal
from django.contrib.auth.models import User

def getStringFromInput(form, s):
    """ Retrieves the string value from the input field in the given form  """
    data = form.cleaned_data[s]
    return None if data is None else data.strip()

def index(request):
    context = RequestContext(request)
    deals = Deal.objects.all().select_related('UserProfile_Profile')

    form = SearchDealForm(data=request.GET)

    #if nothing is entered/ selected, display top 5 deals
    #else, search.

    if request.method == 'GET' and form.is_valid():
        search_key = getStringFromInput(form, 'search')
        min_price  = form.cleaned_data['min_price']
        max_price  = form.cleaned_data['max_price']
        start      = form.cleaned_data['start_date']
        end        = form.cleaned_data['end_date']
        category   = form.cleaned_data['category']

        #https://docs.djangoproject.com/en/dev/ref/models/querysets/
        q = Q()
        if search_key:
            q |= Q(title__contains=search_key)
            q |= Q(short_desc__contains=search_key)
            q |= Q(description__contains=search_key)

        if min_price:  q &= Q(cost_per_unit__gte=float(min_price))
        if max_price:  q &= Q(cost_per_unit__lte=float(max_price))
        if start:      q &= Q(start_date__gte=start)
        if end:        q &= Q(end_date__lte=end)
        if category:   q &= Q(category_id__exact=category.id)

        deals = Deal.objects.filter(q)


    context_dict = {'deals': deals,
                    'search_form': form }


    return render_to_response('deal_index.html', context_dict, context)

def create_deal_check_login(request):
    #redirect if not logged in
    if not request.user.is_authenticated():
       return HttpResponseRedirect('/account/login')

    success = False
    form = CreateDealForm()
    search_form = SearchDealForm()

    if request.method == 'POST':
       form = CreateDealForm(request.POST)
       if form.is_valid():
           deal = form.save(commit=False)
           deal.owner_id = request.user.id
           deal.save()
           success = True
    return render(request, 'create_deal.html', { 'form': form,
                                                 'request': request,
                                                 'search_form': search_form,
                                                 'valid_form': success},)
def detail(request, pk):
    try:
        deal = Deal.objects.get(id=pk)
        owner = User.objects.get(id=deal.owner_id)
    except ObjectDoesNotExist:
        deal = None
        owner = None

    context_dict = {'deal': deal,
                    'owner': owner,}
    return render(request, 'deal_detail.html', context_dict)
