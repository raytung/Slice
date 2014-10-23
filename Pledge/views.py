from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.core.urlresolvers import reverse



from UserProfile.models import Profile
from Pledge.forms import CommitmentForm
from Pledge.models import Commitment

from django.db.models import Sum
from django.shortcuts import redirect

# Create your views here.

def pledge_edit(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login?next=' + request.path )
    profile = Profile.objects.get(account_id=request.user.id)

    try:
        pledge = profile.commitment_set.get(deal=pk)
    except ObjectDoesNotExist:
        pledge = None
    if not pledge: return render(request, 'pledge_edit.html', {'pledge': pledge,
                                                                'error_message': "No commitment found"})
    deal = pledge.deal
    is_expired = (deal.end_date < timezone.localtime(timezone.now()))
    if is_expired:
        error_message = "Deal has already expired. You cannot modify your commitment"
    success = False
    error_message = None
    units_remained = deal.num_units
    claimed_units = Commitment.objects.filter(deal_id=deal.id).aggregate(Sum('units'))
    units_remained -= claimed_units['units__sum']

    if 'save-pledge' in request.POST:
        form = CommitmentForm(request.POST, instance=pledge)
        if form.is_valid():
            if units_remained < form.cleaned_data['units']:
                error_message = "The deal does not have enough units to go around! Try reducing your units"
            else:
                commitment = form.save(commit=False)
                commitment.last_modified_date = timezone.localtime(timezone.now())
                commitment.save()
                success = True
    elif 'delete-pledge' in request.POST:
        if timezone.localtime(timezone.now()) >= deal.end_date:
            error_message = "You cannot retract now. Deal has ended."
        else:
            pledge.delete()
            return redirect('profile_myslice')
    elif 'submit-cancel' in request.POST:
        return HttpResponseRedirect(reverse('deals_index'))
    else:
        form = CommitmentForm(instance=pledge)



    return render(request, 'pledge_edit.html', {'pledge':pledge,
                                                'form':form,
                                                'deal':deal,
                                                'is_expired': is_expired,
                                                'saved': success, 
                                                'error_message': error_message,
                                                'units_remained': units_remained})
