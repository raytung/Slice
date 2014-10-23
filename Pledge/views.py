from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


from UserProfile.models import Profile
from Pledge.forms import CommitmentForm

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
    is_expired = (deal.end_date < timezone.now())
    if is_expired:
        error_message = "Deal has already expired. You cannot modify your commitment"
    success = False

    if request.POST:
        form = CommitmentForm(request.POST, instance=pledge)
        if form.is_valid():
            commitment = form.save(commit=False)
            commitment.last_modified_date = timezone.now()
            commitment.save()
            success = True
    else:
        form = CommitmentForm(instance=pledge)



    return render(request, 'pledge_edit.html', {'pledge':pledge,
                                                'form':form,
                                                'deal':deal,
                                                'is_expired': is_expired,
                                                'saved': success})
