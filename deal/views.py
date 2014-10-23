from django.shortcuts import render, redirect
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
from deal.forms  import CreateDealForm, SearchDealForm, RateDealForm, UploadImageForm, EditDealForm
from deal.models import Deal, Rating
from django.contrib.auth.models import User
from UserProfile.models import Profile, History
from Pledge.forms import CommitmentForm
from Pledge.models import Commitment

from Slice.helper import get_sorted_model, get_paginator


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
            q |= Q(title__iexact=search_key)
            q |= Q(short_desc__contains=search_key)
            q |= Q(description__contains=search_key)

        if min_price:  q &= Q(cost_per_unit__gte=float(min_price))
        if max_price:  q &= Q(cost_per_unit__lte=float(max_price))
        if start:      q &= Q(start_date__gte=start)
        if end:        q &= Q(end_date__lte=end)
        if category:   q &= Q(category_id__exact=category.id)

        deals = Deal.objects.filter(q)
    now = timezone.localtime(timezone.now())

    deals = get_sorted_model(request, deals)
    deals, last_page = get_paginator(deals, request)


    context_dict = {'deals': deals,
                    'search_form': form,
                    'now': now,
                    'last_page':last_page}


    return render_to_response('deal_index.html', context_dict, context)

def is_valid_dates(start, end):
    now = timezone.localtime(timezone.now())
    return start >= now and end > now and start < end


def create_deal_check_login(request):
    if not request.user.is_authenticated():
    #redirect to login page
       return HttpResponseRedirect('/account/login?next=' + request.path )

    success = False
    form = CreateDealForm()
    search_form = SearchDealForm()

    if request.method == 'POST':
       form = CreateDealForm(request.POST, request.FILES)

       if form.is_valid():
           deal = form.save(commit=False)
           deal.owner_id = request.user.id
           deal.available_units = deal.num_units
           img = request.FILES.get('thumbnail', None)
           deal.thumbnail = img if img else "default.svg"
           deal.save()
           success = True
       else:
            print form.errors
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
            now = timezone.localtime(timezone.now())
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
                pledge.last_modified_date= timezone.localtime(timezone.now())
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

    is_expired = (found_deal.end_date < timezone.localtime(timezone.now()))

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


def edit_deal (request, pk):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path)

    deal_entry = Deal.objects.get(id=pk)
    if request.user.id != deal_entry.owner_id:
        error_message = "You do not have right to modify this deal"
        return render(request, 'edit_deal.html', {'error_message':error_message})
    if request.method == 'POST':
        form = EditDealForm(request.POST, request.FILES, instance=deal_entry)

        if form.is_valid():
            form.save()
            return redirect('profile_mydeals')
    else:
        form = EditDealForm(initial={'title':deal_entry.title,
                                 'short_desc':deal_entry.short_desc,
                                 'description':deal_entry.description,
                                 'category':deal_entry.category,
                                 'cost_per_unit':deal_entry.cost_per_unit,
                                 'num_units':deal_entry.num_units,
                                 'available_units':deal_entry.available_units,
                                 'savings_per_unit':deal_entry.savings_per_unit,
                                 'start_date':deal_entry.start_date,
                                 'end_date':deal_entry.end_date,
                                 'delivery_method':deal_entry.delivery_method,
                                 'thumbnail': deal_entry.thumbnail
                                 })

    return render(request, 'edit_deal.html', {'edit_form': form,
                                              'deal': deal_entry
                                              })

def deal_view_pledges(request, pk):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path)
    try:
        deal_entry = Deal.objects.get(id=pk)
    except ObjectDoesNotExist:
        deal_entry = None

    if not deal_entry:
        error_message = "You do not have access rights this page"
        return render(request, 'deal_view_pledges.html', {'error_message':error_message})


    if request.user.id != deal_entry.owner_id:
        error_message = "You do not have access rights this page"
        return render(request, 'deal_view_pledges.html', {'error_message':error_message})

    user_profiles = Profile.objects.select_related('account').filter(commitment__deal_id=pk)
    for p in user_profiles:
        print p.account.user.email
        print p.commitment_set.get(deal=deal_entry)


    context_dict = {'user_profiles': user_profiles,
                    'pk': int(pk)}

    return render(request, 'deal_view_pledges.html', context_dict)

