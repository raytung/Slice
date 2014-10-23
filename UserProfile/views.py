from django.shortcuts     import render, redirect
from django.http          import HttpResponse, HttpResponseRedirect
from django.template      import RequestContext
from django.shortcuts     import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
#https://docs.djangoproject.com/en/dev/topics/pagination/
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import ListView


#Pinax
from account import urls, models

from UserProfile.models import Profile, History
from UserProfile.forms import EditAccountForm, EditDescriptionForm, EditContactForm
from deal.models import Deal

def get_piginator(obj, request):
  piginator  = Paginator(obj, 5)
  page = request.GET.get('page')
  try:
      temp = piginator.page(page)
  except PageNotAnInteger:
      temp = piginator.page(1)
  except EmptyPage:
      temp = piginator.page(piginator.num_pages)
  return temp, piginator.num_pages

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
        return HttpResponseRedirect('/account/login?next=' + request.path )

    user = request.user
    user_account = models.Account.objects.get(user_id=user.id)

    try:
        profile = Profile.objects.get(account_id=user_account.id)
    except Profile.DoesNotExist:
        profile = Profile.objects.create_profile(user_account)

    return render(request, 'profile_index.html', { 'profile': profile,
                                                   'user':    user,
                                                  })
def edit_profile(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

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

    form = EditAccountForm(initial={'first_name': user.first_name,
                                    'last_name': user.last_name})

    return render(request, 'profile_edit.html', {'edit_form': form })

def edit_description(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

    user = request.user
    user_account = models.Account.objects.get(user_id=user.id)
    user_profile = Profile.objects.get(account_id=user_account.id)

    if request.method == 'POST':
        form = EditDescriptionForm(request.POST, instance=user_profile)
        if form.is_valid():
            acc = form.save(commit=False)

            #telling Django that we're only updating these 2 fields in the model
            acc.save(update_fields=["description"])
            #need to redirect so we won't get stuck at POST.
            #try removing the following line and test out the save function.
            #after you saved, try refreshing the page.
            return redirect('profile_index')

    form = EditDescriptionForm(initial={'description': user_profile.description})

    return render(request, 'profile_edit_description.html', {'edit_form': form })

def edit_contact(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

    user = request.user
    user_account = models.Account.objects.get(user_id=user.id)
    user_profile = Profile.objects.get(account_id=user_account.id)

    if request.method == 'POST':
        form = EditContactForm(request.POST, instance=user_profile)
        if form.is_valid():
            acc = form.save(commit=False)

            #telling Django that we're only updating these 2 fields in the model
            acc.save(update_fields=["mobile_number",
                                    "contact_info"])
            #need to redirect so we won't get stuck at POST.
            #try removing the following line and test out the save function.
            #after you saved, try refreshing the page.
            return redirect('profile_index')

    form = EditContactForm(initial={'mobile_number': user_profile.mobile_number,
                                    'contact_info': user_profile.contact_info})

    return render(request, 'profile_edit_contact.html', {'edit_form': form })

def my_deals(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

    deals = Deal.objects.filter(owner_id=request.user.id)
    piginated_obj, last_page = get_piginator(deals, request)

    context_dict = {'deals': piginated_obj,
                    'last_page': last_page}

    return render(request, 'profile_mydeals.html', context_dict)

def history(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

    history = Deal.objects.filter(history__user_id=request.user.id)

    piginated_obj, last_page = get_piginator(history, request)
    context_dict = {'deals': piginated_obj,
                    'last_page': last_page}

    return render(request, 'profile_history.html', context_dict)

def myslice(request):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )
    deals = Deal.objects.filter(commitment__user_id=request.user.id)

    piginated_obj, last_page = get_piginator(deals, request)

    context_dict = {'deals': piginated_obj,
                    'last_page': last_page}


    return render(request, 'profile_myslice.html', context_dict)

def bookmarks(request, **kwargs):
    if not request.user.is_authenticated():
        #redirect to login page
        return HttpResponseRedirect('/account/login?next=' + request.path )

    current_viewer = Profile.objects.get(account_id=request.user.id)
    bookmark = current_viewer.bookmarks.all()
    sort = request.GET.get('sort', None)
    print sort

    if sort == "price_lth":
        bookmark = bookmark.order_by('cost_per_unit')
    elif sort == "price_htl":
        bookmark = bookmark.order_by('-cost_per_unit')
    elif sort == "end_lth":
        bookmark = bookmark.order_by('end_date')
    elif sort =="end_htl":
        bookmark = bookmark.order_by('-end_date')
    elif sort == "alpha_lth":
        bookmark = bookmark.order_by('-title')
    elif sort == "alpha_htl":
        bookmark = bookmark.order_by('title')
    elif sort == "end_date_lth":
        bookmark = bookmark.order_by('end_date')
    elif sort == "end_date_htl":
        bookmark = bookmark.order_by('-end_date')
    elif sort == "start_date_lth":
        bookmark = bookmark.order_by('start_date')
    elif sort == "start_date_htl":
        bookmark = bookmark.order_by('-start_date')

    print bookmark


    piginated_obj, last_page = get_piginator(bookmark, request)

    context_dict = {'deals': piginated_obj,
                    'last_page': last_page}

    return render(request, 'profile_bookmarks.html', context_dict)
