from django.shortcuts import render

from UserProfile.models import Profile
from account.models import Account

# Create your views here.

def users_detail(request, pk):
    account = Account.objects.get(id=pk)
    profile = Profile.objects.get(account_id=pk)

    return render(request, 'users_detail.html', {'user': account.user,
                                                 'profile': profile})
