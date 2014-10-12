from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.template  import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

#https://docs.djangoproject.com/en/1.7/topics/db/queries/#complex-lookups-with-q-objects
from django.db.models import Q

#Pinax
from account import urls

#Models
from deal.forms  import CreateDealForm, SearchDealForm
from deal.models import Deal
from django.contrib.auth.models import User
from UserProfile.models import Profile, History
from Pledge.forms import CommitmentForm
from Pledge.models import Commitment

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

def is_valid_pledge(pledge_form, deal):
    time_commited = timezone.now()
    units = pledge_form.cleaned_data['units']
    return (deal.end_date >= time_commited and \
        deal.available_units >= units and \
        deal.min_pledge_amount <= units)


def detail(request, pk):
    try:
        found_deal = Deal.objects.get(id=pk)
        current_viewer = Profile.objects.get(account_id=request.user.id)
        history = History(user=current_viewer, deal=found_deal)
        history.save()
        has_pledged = Commitment.objects.filter(deal_id=pk, user_id=request.user.id)

        pledge_form = CommitmentForm()
        if request.method == 'POST':
            pledge_form = CommitmentForm(request.POST)
            if pledge_form.is_valid() and is_valid_pledge(pledge_form, found_deal) :
                pledge = pledge_form.save(commit=False)
                pledge.last_modified_date= timezone.now()
                pledge.user = current_viewer
                pledge.deal = found_deal
                pledge.save()
                found_deal.available_units -= pledge.units
                found_deal.save()
                has_pledged = Commitment.objects.filter(deal_id=pk, user_id=request.user.id)

        owner = User.objects.get(id=found_deal.owner_id)
    except ObjectDoesNotExist:
        found_deal = None
        owner = None

    context_dict = {'deal': found_deal,
                    'owner': owner,
                    'pledge_form': pledge_form,
                    'has_pledged': has_pledged,}
    return render(request, 'deal_detail.html', context_dict)
