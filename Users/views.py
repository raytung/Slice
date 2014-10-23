from django.shortcuts import render

from UserProfile.models import Profile
from account.models import Account
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def users_detail(request, pk):
    error_message, account, profile = None, None, None

    try:
        account = Account.objects.get(id=pk)
        profile = Profile.objects.get(account_id=pk)
    except ObjectDoesNotExist:
        error_message = "User not found."

    return render(request, 'users_detail.html', {'error_message': error_message,
                                                 'account': account,
                                                 'profile': profile})
