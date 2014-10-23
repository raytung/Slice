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
from django.db.models import Q, Avg, Sum

#Pinax
from account import urls

#Models
from deal.forms  import CreateDealForm, SearchDealForm, RateDealForm
from deal.models import Deal, Rating
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
    deals = Deal.objects.all()


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

def is_valid_dates(start, end):
    return start >= timezone.now() and end > timezone.now() and start < end


def create_deal_check_login(request):
    if not request.user.is_authenticated():
    #redirect to login page
       return HttpResponseRedirect('/account/login?next=' + request.path )

    success = False
    form = CreateDealForm()
    search_form = SearchDealForm()

    if request.method == 'POST':
       form = CreateDealForm(request.POST)
       if form.is_valid():
           deal = form.save(commit=False)
           deal.owner_id = request.user.id
           deal.available_units = deal.num_units
           deal.save()
           success = True
    return render(request, 'create_deal.html', { 'form': form,
                                                 'request': request,
                                                 'search_form': search_form,
                                                 'valid_form': success},)

def detail(request, pk):
    try:
        found_deal = Deal.objects.get(id=pk)
    except:
        found_deal = None
    if not found_deal: return render(request, 'deal_detail.html', {'deal':found_deal, 
                                                                   'error_message': "No deal is found. Did you enter the correct URL?"})

    signed_in = request.user.is_authenticated()
    current_viewer = None if not signed_in else Profile.objects.get(account_id=request.user.id)
    deal_owner = User.objects.get(id=found_deal.owner_id)
    pledge_form = CommitmentForm()
    rate_form = RateDealForm()
    error_message = None


    # don't want double history on bookmarking/pledging
    # will have double history on refresh though
    if signed_in and request.method != 'POST':
        History(user=current_viewer, deal=found_deal).save()

    try:
        has_pledged = Commitment.objects.filter(deal_id=pk, user_id=request.user.id)
    except ObjectDoesNotExist:
        has_pledged = False

    claimed_units = Commitment.objects.filter(deal_id=found_deal.id).aggregate(Sum('units'))
    #in case no claimed units yet
    if claimed_units['units__sum'] == None:
        units_left = found_deal.num_units
    else:
        units_left = found_deal.num_units - claimed_units['units__sum']

    if 'submit-pledge' in request.POST:
        pledge_form = CommitmentForm(request.POST)
        if pledge_form.is_valid():
            request_units = pledge_form.cleaned_data['units']
            now = timezone.now()
            if request_units > units_left:
                error_message = "There are not enough units to go around. Please reduce your units"
            elif now > found_deal.end_date:
                error_message = "You cannot pledge anymore. The deal has expired!"
            elif found_deal.start_date > now:
                error_message = "You cannot pledge yet. Please wait till the deal starts!"
            elif found_deal.min_pledge_amount > request_units:
                error_message = "You need to pledge at least " + str(deal.min_pledge_amount) + " unit!"
            else:
                pledge = pledge_form.save(commit=False)
                pledge.last_modified_date= timezone.now()
                pledge.user = current_viewer
                pledge.deal = found_deal
                pledge.save()

                has_pledged = True
    elif 'bookmark' in request.POST:
        current_viewer.bookmarks.add(found_deal)
    elif 'remove-bookmark' in request.POST:
        current_viewer.bookmarks.remove(found_deal)
    elif 'rate-deal' in request.POST:
        rate_form = RateDealForm(request.POST)
        if rate_form.is_valid():
            try:
                rate = Rating.objects.get(deal=found_deal, user=current_viewer)
            except ObjectDoesNotExist:
               rate = Rating.objects.create(deal=found_deal, user=current_viewer)
            rate.rating = rate_form.cleaned_data['rating']
            rate.save()

    bookmark = []
    if signed_in and current_viewer:
        try:
            bookmark = current_viewer.bookmarks.get(id=found_deal.id)
        except ObjectDoesNotExist:
            bookmark = None
    else:
        pledge_form = None
        has_pledged = False

    current_rating = Rating.objects.filter(deal=found_deal)

    if current_rating:
        avg_rating = current_rating.aggregate(Avg('rating'))
        avg_rating = avg_rating['rating__avg']
    else:
        avg_rating = "This deal has no ratings yet. Be the first one to rate it!"

    is_expired = (found_deal.end_date < timezone.now())

    if is_expired: error_message = "Deal has expired"


    context_dict = {'deal': found_deal,
                    'owner': deal_owner,
                    'pledge_form': pledge_form,
                    'has_pledged': has_pledged,
                    'bookmark': bookmark,
                    'signed_in': signed_in,
                    'rate_form': rate_form,
                    'avg_rating': avg_rating,
                    'is_expired': is_expired,
                    'units_left': units_left,
                    'user': request.user,
                    'error_message': error_message}
    return render(request, 'deal_detail.html', context_dict)
